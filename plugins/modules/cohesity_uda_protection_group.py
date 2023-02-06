#!/usr/bin/python
# Copyright (c) 2022 Cohesity Inc


from __future__ import absolute_import, division, print_function

__metaclass__ = type

# GNU General Public License v3.0+ (see https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = """
---
author: "Naveena (@naveena-maplelabs)"
description:
  - "Ansible Module used to register, remove, start, and stop the Cohesity Protection Group on a Cohesity Cluster."
  - "When executed in a playbook, the Cohesity Protection Group will be validated and the appropriate state action"
  - "will be applied."
module: cohesity_uda_protection_group
options:
  cancel_active:
    default: false
    description:
      - "Specifies if Current Running Backup Group should be canceled.  If False, active groups will not be stopped"
      - "and a failure will be raised."
      - "Optional and only valid when I(state=stopped)"
    type: bool
  cluster:
    aliases:
      - cohesity_server
    description:
      - "IP or FQDN for the Cohesity Cluster"
    type: str
  cohesity_admin:
    aliases:
      - admin_name
      - cohesity_user
      - username
    description:
      - Username with which Ansible will connect to the Cohesity Cluster. Domain Specific credentails can be configured in following formats
      - username@AD.domain.com
      - AD.domain.com/username@tenant
      - LOCAL/username@tenant
      - Domain/username (Will be deprecated in future)
    type: str
  cohesity_password:
    aliases:
      - password
      - admin_pass
    description:
      - "Password belonging to the selected Username.  This parameter will not be logged."
    type: str
  delete_backups:
    default: false
    description:
      - "Specifies if Snapshots generated by the Protection Group should also be deleted when the Group is deleted."
      - "Optional and only valid when I(state=absent)"
    type: bool
  description:
    description:
      - "Optional Description to assign to the Protection Group"
    type: str
  endpoint:
    type: str
    description: Ip address of the Uda host.
  environment:
    default: UDA
    description:
      - "Specifies the environment type of the group."
    required: false
    type: str
  full_backup_args:
    type: str
    description:
      - Specifies the custom arguments to be supplied to the full
        backup script when a full backup is enabled in the policy.
    default: ""
  incr_backup_args:
    type: str
    description:
      - Specifies the custom arguments to be supplied to the incremental
        backup script when an incremental backup is enabled in the policy.
    default: ""
  log_backup_args:
    type: str
    description:
      - Specifies the custom arguments to be supplied to the log backup
        script when a log backup is enabled in the policy.
    default: ""
  concurrency:
    description:
      - Specifies the maximum number of concurrent IO Streams that will
        be created to exchange data with the cluster.
    default: 1
    type: int
  mounts:
    description:
      - Specifies the maximum number of view mounts per host.
    type: int
    default: 1
  name:
    aliases:
      - protection_group_name
    description:
      - "Name to assign to the Protection Group"
    required: true
    type: str
  objects:
    type: list
    elements: str
    description: "Defines the list of objects to be protected."
  ondemand_run_type:
    choices:
      - Regular
      - Full
      - Log
      - System
    default: Regular
    description:
      - "Specifies the type of OnDemand Backup."
    type: str
  protection_policy:
    aliases:
      - policy
    default: Bronze
    description:
      - "Valid policy name or ID for andexisting Protection Policy to be assigned to the group."
      - "Required when I(state=present)."
    type: str
  start_time:
    description:
      - "Specifies the registered start time for the Protection Group.  Format must be 24hr time in either HHMM or HH:MM style."
      - "If not configured then the Cluster will automatically select a time."
    type: str
    default: 00:00
  state:
    choices:
      - present
      - absent
      - started
      - stopped
    default: present
    description:
      - "Determines the state of the Protection Group"
    type: str
  storage_domain:
    default: DefaultStorageDomain
    description:
      - "Existing Storage Domain to which the Protection Group will be associated. Required when I(state=present)."
    type: str
  time_zone:
    default: America/Los_Angeles
    description:
      - "Specifies the timezone to use when calculating time for this Protection Group such as the Group start time."
    type: str
  validate_certs:
    default: false
    description:
      - "Switch determines if SSL Validation should be enabled or not."
    type: bool
  is_paused:
    default: true
    description:
      - "Switch determines whether the newly created job run should be enabled or not."
    type: bool
extends_documentation_fragment:
- cohesity.dataprotect.cohesity
short_description: "Management of Cohesity UDA Protection Groups"
version_added: 1.0.10
"""

EXAMPLES = """
# Create a new UDA Protection Group
- cohesity_uda_group:
    cluster: cohesity.lab
    username: admin
    password: password
    state: present
    name: myhost
    endpoint: cohesity-source-ip
    protection_policy: Bronze
    storage_domain: Default

"""

RETURN = """
# Returns the registered Protection Group ID
"""

import json
import time


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import open_url, urllib_error


from cohesity_management_sdk.exceptions.api_exception import APIException
from cohesity_management_sdk.models.delete_protection_job_param import (
    DeleteProtectionJobParam,
)
from cohesity_management_sdk.models.cancel_protection_job_run_param import (
    CancelProtectionJobRunParam,
)
from cohesity_management_sdk.models.run_protection_job_param import (
    RunProtectionJobParam,
)


try:
    # => When unit testing, we need to look in the correct location however, when run via ansible,
    # => the expectation is that the modules will live under ansible.
    from ansible.module_utils.urls import urllib_error
    from ansible_collections.cohesity.dataprotect.plugins.module_utils.cohesity_auth import (
        get__cohesity_auth__token,
    )
    from ansible_collections.cohesity.dataprotect.plugins.module_utils.cohesity_utilities import (
        cohesity_common_argument_spec,
        raise__cohesity_exception__handler,
        REQUEST_TIMEOUT,
    )
    from ansible_collections.cohesity.dataprotect.plugins.module_utils.cohesity_hints import (
        get_cohesity_client,
        get__prot_source_id__by_endpoint,
        get__prot_policy_id__by__name,
        get__storage_domain_id__by__name,
        get_protection_run__status__by_id,
        check__protection_group__exists,
        check_source_reachability,
        get__prot_policy_id__by_name,
        get__storage_domain_id__by_name,
    )
except Exception:
    pass


class ParameterViolation(Exception):
    pass


class ProtectionException(Exception):
    pass


def get_source_id_by_endpoint(module):
    """
    Function to fetch source id using endpoint.
    return: source id
    """
    try:
        endpoint = module.params.get("endpoint")
        env = "k" + module.params.get("environment")
        resp = cohesity_client.protection_sources.list_protection_sources(
            environments=env
        )
        if resp:
            parent_id = resp[0].protection_source.id
            nodes = resp[0].nodes
            for node in nodes:
                if node["protectionSource"]["name"] == endpoint:
                    source = node["protectionSource"]
                    return parent_id, source["id"]
        return None, None
    except Exception as error:
        raise__cohesity_exception__handler(error, module)


def check__mandatory__params(module):
    """
    This method will perform validations of optionally mandatory parameters
    required for specific states and environments.
    """
    success = True
    missing_params = list()
    environment = module.params.get("environment")

    if module.params.get("state") == "present":
        action = "creation"

        if not module.params.get("endpoint"):
            success = False
            missing_params.append("endpoint")
        if not module.params.get("protection_policy"):
            success = False
            missing_params.append("protection_policy")
        if not module.params.get("storage_domain"):
            success = False
            missing_params.append("storage_domain")

    else:
        action = "remove"

    if not success:
        module.fail_json(
            msg="The following variables are mandatory for this action ("
            + action
            + ") when working with environment type ("
            + environment
            + ")",
            missing=missing_params,
        )


def wait__for_group_state__transition(module, group_id, state="start"):
    if state != "start":
        state = "stop"
    loop_cnt = 0
    while loop_cnt <= 3:
        # => If the backup finishes before we check, we need to look
        # => at previous backups to see if the last group is successful.
        currently_active, status, last_run = get_protection_run__status__by_id(
            module, group_id
        )
        if state == "start" and status == "kAccepted":
            return
        elif state == "stop" and status in ["kSuccess", "kCanceled"]:
            return
        else:
            time.sleep(5)
            loop_cnt += 1

    if loop_cnt == 21:
        module.fail_json(
            msg="Failed to successfully " + state + " the Cohesity Protection Group",
            changed=False,
            id=group_id,
            loop_cnt=loop_cnt,
        )


def start_group(module, details):
    # => Get group id.
    group_exists, group = check__protection_group__exists(module, details)
    if not group_exists:
        name = module.params.get("name")
        results = dict(
            changed=False,
            msg="Protection Group with name " + name + " is not available.",
        )
        module.exit_json(**results)
    group_id = group.uid.id
    currently_active, status, last_run = get_protection_run__status__by_id(
        module, group_id
    )
    if currently_active:
        results = dict(
            changed=False,
            msg="The Protection Group for this host is currently running",
            name=module.params.get("name"),
        )
        module.exit_json(**results)

    try:
        body = RunProtectionJobParam()
        body.run_type = "k" + module.params.get("ondemand_run_type")
        cohesity_client.protection_groups.create_run_protection_group(group_id, body)

        # => This dictionary will allow us to return a standardized output
        # => for all Protection Group.
        output = dict(id=group_id)

        # => It can take a few moments for the group to actually stop.  In this case,
        # => We will introduce a delay and check every (5) seconds for up to a minute
        # => to see if the group stopped.
        wait__for_group_state__transition(module, group_id, state="start")

        return output
    except urllib_error.URLError as e:
        # => Capture and report any error messages.
        raise__cohesity_exception__handler(e.read(), module)
    except Exception as error:
        raise__cohesity_exception__handler(error, module)


def stop_group(module, _id):
    currently_active, status, last_run = get_protection_run__status__by_id(module, _id)
    if not currently_active:
        results = dict(
            changed=False,
            msg="The Protection Group for this host is not currently running",
            name=module.params.get("name"),
        )
        module.exit_json(**results)
    if not module.params.get("cancel_active") and currently_active:
        module.fail_json(
            changed=False,
            msg="The Protection Group for this host is active and cannot be stopped",
        )
    try:

        output = dict(
            id=_id, cancel_active=module.params.get("cancel_active"), groupRunIds=list()
        )
        body = CancelProtectionJobRunParam()
        body.group_run_id = last_run.backup_run.group_run_id
        cohesity_client.protection_runs.create_cancel_protection_group_run(_id, body)

        # => It can take a few moments for the group to actually stop.  In this case,
        # => We will introduce a delay and check every (5) seconds for up to a minute
        # => to see if the group stopped.
        wait__for_group_state__transition(module, _id, state="stop")

        return output
    except Exception as error:
        raise__cohesity_exception__handler(error, module)


def create_group(module, self, body):
    server = module.params.get("cluster")
    validate_certs = module.params.get("validate_certs")
    token = self["token"]
    try:
        request_type = "POST"
        uri = "https://" + server + "/v2/data-protect/protection-groups"
        if self["group_exists"]:
            uri += "/" + self["group_exists"]
            request_type = "PUT"
        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer " + token,
            "user-agent": "cohesity-ansible/v1.0.10",
        }
        response = open_url(
            url=uri,
            method=request_type,
            data=json.dumps(body),
            headers=headers,
            validate_certs=validate_certs,
            timeout=REQUEST_TIMEOUT,
        )
        if not response.getcode() not in [201, 204]:
            raise Exception(
                "Failed to create/update the protection group, err '%s'"
                % response.read()
            )
        response = json.loads(response.read())
        return response
    except urllib_error.URLError as e:
        # => Capture and report any error messages.
        raise__cohesity_exception__handler(e.read(), module)
    except Exception as error:
        raise__cohesity_exception__handler(error, module)


def unregister_group(module, _id):
    """
    Unregister a protection group.
    """
    try:
        body = DeleteProtectionJobParam()
        body.delete_snapshots = module.params.get("delete_backups")
        resp = cohesity_client.protection_groups.delete_protection_group(_id, body)
        return resp
    except Exception as error:
        raise__cohesity_exception__handler(error, module)


def main():
    # => Load the default arguments including those specific to the Cohesity Protection Groups.
    argument_spec = cohesity_common_argument_spec()
    argument_spec.update(
        dict(
            state=dict(
                choices=["present", "absent", "started", "stopped"], default="present"
            ),
            name=dict(type="str", required=True, aliases=["protection_group_name"]),
            description=dict(type="str", default=""),
            environment=dict(default="UDA"),
            protection_policy=dict(type="str", aliases=["policy"], default="Bronze"),
            storage_domain=dict(type="str", default="DefaultStorageDomain"),
            time_zone=dict(type="str", default="America/Los_Angeles"),
            start_time=dict(type="str", default="00:00"),
            delete_backups=dict(type="bool", default=False),
            is_paused=dict(type="bool", default=True),
            cancel_active=dict(type="bool", default=False),
            validate_certs=dict(type="bool", default=False),
            endpoint=dict(type="str", default=""),
            objects=dict(type="list", default=[], elements="str"),
            concurrency=dict(type="int", default=1),
            mounts=dict(type="int", default=1),
            full_backup_args=dict(type="str", default=""),
            incr_backup_args=dict(type="str", default=""),
            log_backup_args=dict(type="str", default=""),
            ondemand_run_type=dict(
                type="str",
                default="Regular",
                choices=["Regular", "Full", "Log", "System"],
            ),
        )
    )

    global token
    global cohesity_client
    # => Create a new module object
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)
    cohesity_client = get_cohesity_client(module)
    token = get__cohesity_auth__token(module)

    results = dict(
        changed=False,
        msg="Attempting to manage Protection Source",
        state=module.params.get("state"),
    )
    api_details = dict(token=token, timeout=REQUEST_TIMEOUT)
    group_exists, group_meta_data = check__protection_group__exists(module, api_details)

    if module.check_mode:
        check_mode_results = dict(
            changed=False,
            msg="Check Mode: Cohesity Protection Group is not currently registered",
            id="",
        )
        if module.params.get("state") == "present":
            job_details = dict(
                token=get__cohesity_auth__token(module),
                name=module.params.get("name"),
                environment=module.params.get("environment"),
                sourceIds=module.params.get("endpoint"),
                policyId=module.params.get("protection_policy"),
                viewBoxId=module.params.get("storage_domain"),
                timezone=module.params.get("time_zone"),
            )
            if group_exists:
                check_mode_results[
                    "msg"
                ] = "Check Mode: Cohesity Protection Group is currently registered.  No changes"
            else:
                check_mode_results[
                    "msg"
                ] = "Check Mode: Cohesity Protection Group is not currently registered.  This action would register the Cohesity Protection Group."
                check_mode_results["id"] = group_exists
                # Check the endpoint reachability.
                status = check_source_reachability(module.params.get("endpoint"))
                if not status:
                    if status is None:
                        check_mode_results["msg"] += (
                            "Please ensure cohesity agent is installed in the source '%s' and port 50051 is open."
                            % module.params.get("endpoint")
                        )
                    else:
                        check_mode_results[
                            "msg"
                        ] += "Source '%s' is not reachable." % module.params.get(
                            "endpoint"
                        )
                if not get__prot_policy_id__by_name(module, job_details):
                    check_mode_results["msg"] += (
                        "Protection policy '%s' is not available in the cluster"
                        % module.params.get("policy")
                    )
                if not get__storage_domain_id__by_name(module, job_details):
                    check_mode_results["msg"] += (
                        "Storage domain '%s' is not available in the cluster"
                        % module.params.get("storage_domain")
                    )
        else:
            if group_exists:
                check_mode_results[
                    "msg"
                ] = "Check Mode: Cohesity Protection Group is currently registered.  This action would unregister the Cohesity Protection Group."
                check_mode_results["id"] = group_exists
            else:
                check_mode_results[
                    "msg"
                ] = "Check Mode: Cohesity Protection Group is not currently registered.  No changes."
        module.exit_json(**check_mode_results)

    elif module.params.get("state") == "present":
        group_details = dict(
            token=token, environment="UDA", endpoint=module.params.get("endpoint")
        )
        source_id = get__prot_source_id__by_endpoint(module, group_details)
        if not source_id:
            module.fail_json(
                msg="Source '%s' is not registered to cluster, Please register the source and try again."
                % module.params.get("endpoint")
            )
        check__mandatory__params(module)
        body = dict(
            name=module.params.get("name"),
            storageDomainId=get__storage_domain_id__by__name(module),
            environment="k" + module.params.get("environment"),
            policyId=get__prot_policy_id__by__name(module),
            timezone=module.params.get("time_zone").strip(),
            timeZone=module.params.get("time_zone").strip(),
            description=module.params.get("description"),
        )
        objects = [{"name": name for name in module.params.get("objects")}]
        body["udaParams"] = dict(
            sourceId=source_id,
            objects=objects,
            fullBackupArgs=module.params.get("full_backup_args"),
            incrBackupArgs=module.params.get("incr_backup_args"),
            logBackupArgs=module.params.get("log_backup_args"),
            concurrency=module.params.get("concurrency"),
            mounts=module.params.get("mounts"),
        )

        if module.params.get("start_time"):
            start_time = list(module.params.get("start_time").replace(":", ""))
            if not len(start_time) == 4:
                # => There are only so many options here but if we get more characters
                # => than four then we need to escape quickly.
                module.fail_json(
                    msg="Invalid start_time selected ("
                    + module.params.get("start_time")
                    + ").  Please review and submit the correct Protection Group Starting time."
                )
            body["startTime"] = dict(
                hour=int(start_time[0] + start_time[1]),
                minute=int(start_time[2] + start_time[3]),
            )
        try:
            group_details = dict(token=token, group_exists=group_exists)
            if group_exists:
                response = create_group(module, group_details, body)
                msg = "Updation of Cohesity Protection Group Complete"
            else:
                response = create_group(module, group_details, body)
                msg = "Creation of Cohesity Protection Group Complete"
            response = dict(id=response["id"], name=response["name"])
            results = dict(changed=True, msg=msg, **response)
        except APIException as err:
            module.fail_json(msg=err.message)

    elif module.params.get("state") == "absent":
        if group_exists:
            group_id = group_meta_data.uid.id
            status, is_active, run = get_protection_run__status__by_id(module, group_id)
            if status:
                stop_group(module, group_id)
                while True:
                    status, is_active, run = get_protection_run__status__by_id(
                        module, group_id
                    )
                    if not status:
                        time.sleep(10)
                        break
            response = unregister_group(module, group_exists)

            results = dict(
                changed=True,
                msg="Unregistration of Cohesity Protection Group Complete",
                id=group_exists,
                name=module.params.get("name"),
            )
        else:
            results = dict(
                changed=False,
                msg="The Protection Group for this host is currently not registered",
                name=module.params.get("name"),
            )

    elif module.params.get("state") == "started":
        if group_exists:
            response = start_group(module, api_details)

            results = dict(
                changed=True,
                msg="The Protection Group for this host has been started",
                id=group_exists,
                name=module.params.get("name"),
            )
        else:
            results = dict(
                changed=False,
                msg="The Protection Group for this host is currently not registered",
                name=module.params.get("name"),
            )

    elif module.params.get("state") == "stopped":
        if group_exists:
            group_id = group_meta_data.uid.id
            response = stop_group(module, group_id)

            results = dict(
                changed=True,
                msg="The Protection Group for this host has been stopped",
                id=group_id,
                name=module.params.get("name"),
            )
        else:
            results = dict(
                changed=False,
                msg="The Protection Group for this host is currently not registered",
                name=module.params.get("name"),
            )
    else:
        # => This error should never happen based on the set assigned to the parameter.
        # => However, in case, we should raise an appropriate error.
        module.fail_json(
            msg="Invalid State selected: {0}".format(module.params.get("state")),
            changed=False,
        )

    module.exit_json(**results)


if __name__ == "__main__":
    main()
