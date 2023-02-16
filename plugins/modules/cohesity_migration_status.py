#!/usr/bin/python
# Copyright (c) 2023 Cohesity Inc


from __future__ import absolute_import, division, print_function

__metaclass__ = type

# GNU General Public License v3.0+ (see https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = """
---
author: Naveena (@naveena-maplelabs)
description:
  - Ansible Module used to poll for status of objects in a Cohesity Migration Job
  - When executed in a playbook, the insync sttaus of objects in Cohesity
    migration Job will be returned.
module: cohesity_migration_status
options:
  task_id:
    description:
      - Task Id of the migrate job.
    type: str
  cluster:
    aliases:
      - cohesity_server
    description:
      - IP or FQDN for the Cohesity Cluster
    type: str
  cohesity_admin:
    aliases:
      - admin_name
      - cohesity_user
      - username
    description:
      - Username with which Ansible will connect to the Cohesity Cluster. Domain
        Specific credentails can be configured in following formats
      - AD.domain.com/username
      - AD.domain.com/username@tenant
      - LOCAL/username@tenant
    type: str
  cohesity_password:
    aliases:
      - password
      - admin_pass
    description:
      - Password belonging to the selected Username.  This parameter will not be
        logged.
    type: str
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - Determines the state of the Recovery Job.
      - (C)present a recovery job will be created and started.
      - (C)absent is currently not implemented
    type: str
  task_name:
    description:
      - Name of the recovery task name. Yet to be implemented
    type: str
extends_documentation_fragment:
  - cohesity.dataprotect.cohesity
short_description: Check Sync status of objects available in the VM migration task
version_added: 1.0.10
"""

EXAMPLES = """

# Poll migration status
- name: Get status in the VM migration task
  cohesity_migration_status:
    cluster: cohesity.lab
    username: admin
    password: password
    state: present
    task_name: "Ansible Migrate VM- Get status"

"""

RETURN = """"""


# GNU General Public License v3.0+ (see https://www.gnu.org/licenses/gpl-3.0.txt)


import json

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote
from collections import defaultdict
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import open_url, urllib_error

try:
    # => When unit testing, we need to look in the correct location however, when run via ansible,
    # => the expectation is that the modules will live under ansible.
    from ansible_collections.cohesity.dataprotect.plugins.module_utils.cohesity_auth import (
        get__cohesity_auth__token,
    )
    from ansible_collections.cohesity.dataprotect.plugins.module_utils.cohesity_utilities import (
        cohesity_common_argument_spec,
        raise__cohesity_exception__handler,
        REQUEST_TIMEOUT,
    )
    from ansible_collections.cohesity.dataprotect.plugins.module_utils.cohesity_hints import (
        get__restore_job__by_type,
    )
except ImportError:
    pass


class ParameterViolation(Exception):
    pass


def check__protection_restore__exists(module, self):
    payload = self.copy()
    payload["restore_type"] = "kRecoverVMs"

    restore_tasks = get__restore_job__by_type(module, payload)

    if not restore_tasks:
        return False, False, False
    if module.params.get("task_name"):
        for task in restore_tasks:
            if task["name"] == self["name"]:
                return task["status"], task["id"], task["name"]
    if module.params.get("task_id"):
        task_id = module.params.get("task_id").split(":")[-1]
        for task in restore_tasks:
            if task["id"] == int(task_id):
                return task["status"], task["id"], task["name"]
    return False, False, False


def get_migration_status(module, self):
    """
    Get migrate task status
    :param module: object that holds parameters passed to the module
    :return:
    """
    server = module.params.get("cluster")
    validate_certs = module.params.get("validate_certs")
    token = get__cohesity_auth__token(module)
    try:
        uri = (
            "https://"
            + server
            + "/irisservices/api/v1/restoretasks/%s" % self["task_id"]
        )
        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer " + token,
            "user-agent": "cohesity-ansible/v2.3.4",
        }
        response = open_url(
            url=uri,
            headers=headers,
            validate_certs=validate_certs,
            method="GET",
            timeout=REQUEST_TIMEOUT,
        )
        response = json.loads(response.read())
        return response
    except urllib_error.URLError as e:
        # => Capture and report any error messages.
        raise__cohesity_exception__handler(e.read(), module)
    except Exception as error:
        raise__cohesity_exception__handler(error, module)


def get_task_status(module, task_id):
    """
    Get migrate task status
    :param module: object that holds parameters passed to the module
    :return:
    """
    server = module.params.get("cluster")
    validate_certs = module.params.get("validate_certs")
    token = get__cohesity_auth__token(module)
    try:
        uri = "https://" + server + "/v2/data-protect/recoveries/%s" % task_id
        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer " + token,
            "user-agent": "cohesity-ansible/v2.3.4",
        }
        response = open_url(
            url=uri,
            headers=headers,
            validate_certs=validate_certs,
            method="GET",
            timeout=REQUEST_TIMEOUT,
        )
        response = json.loads(response.read())
        return response
    except urllib_error.URLError as e:
        # => Capture and report any error messages.
        raise__cohesity_exception__handler(e.read(), module)
    except Exception as error:
        raise__cohesity_exception__handler(error, module)


def main():
    # => Load the default arguments including those specific to the Cohesity Protection Jobs.
    argument_spec = cohesity_common_argument_spec()
    argument_spec.update(
        dict(
            task_name=dict(type="str"),
            state=dict(choices=["present", "absent"], default="present"),
            task_id=dict(type="str"),
        )
    )

    # => Create a new module object
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)
    results = dict(
        changed=False,
        msg="Attempting to fetch VM migration status",
        state=module.params.get("state"),
    )

    task_details = dict(
        token=get__cohesity_auth__token(module),
        name=module.params.get("task_name"),
        id=module.params.get("task_id"),
    )

    task_status, task_id, task_name = check__protection_restore__exists(
        module, task_details
    )
    task_details["id"] = task_id
    task_details["name"] = task_name

    if module.check_mode:
        check_mode_results = dict(
            changed=False,
            msg="Check Mode: Cohesity Protection Migrate Job is not currently registered",
            id="",
            status=""
        )
        if module.params.get("state") == "present":
            if task_status == "kInProgress":
                check_mode_results[
                    "msg"
                ] = "Check Mode: Cohesity Protection Migrate Job status check."
            else:
                check_mode_results[
                    "msg"
                ] = "Check Mode: Cohesity Protection Migrate Job is not registered or Finished."

        else:
            check_mode_results[
                "msg"
            ] = "Cohesity Migrate: This feature (absent) has not be implemented yet."
        module.exit_json(**check_mode_results)

    elif module.params.get("state") == "present":
        check_mode_results = dict(msg="")
        if not task_status:
            results = dict(
                changed=False,
                msg="Couldn't find the migrate job '%s'" % (task_name or task_id),
            )
        else:
            task_details["task_id"] = task_id
            response = get_migration_status(module, task_details)
            status = get_task_status(module, module.params.get("task_id"))["status"]
            results = defaultdict(list)
            if response:
                objects = response[0]["restoreTask"].get(
                    "restoreSubTaskWrapperProtoVec", []
                )
                total_objects = len(objects)
                sync_vms = 0
                error_list = []
                task_status = response[0]["restoreTask"]["performRestoreTaskState"][
                    "base"
                ]["publicStatus"].lstrip("k")
                if task_status == "Running":
                    for obj in objects:
                        status = obj["performRestoreTaskState"]["base"][
                            "publicStatus"
                        ].lstrip("k")
                        # Get the object name.
                        vm_name = obj["performRestoreTaskState"]["objects"][0][
                            "entity"
                        ]["displayName"]
                        if status == "OnHold":
                            multi_stage_restore = obj["performRestoreTaskState"].get(
                                "multiStageRestoreTaskState", ""
                            )
                            if multi_stage_restore and multi_stage_restore.get(
                                "syncTimeUsecs", ""
                            ):
                                sync_vms += 1
                            results[status].append(vm_name)
                            if obj["performRestoreTaskState"]["base"].get("error", ""):
                                error_list.append(
                                    obj["performRestoreTaskState"]["base"]["error"][
                                        "errorMsg"
                                    ]
                                )

                if len(results.keys()) > 1:
                    msg = "Migration is in-progress, one or more VM is still %s." % (
                        "/".join(results.keys())
                    )
                    module.exit_json(
                        msg=msg,
                        changed=False,
                        results=results,
                        status=task_status,
                        errors=error_list,
                    )
                elif results:
                    if sync_vms == total_objects:
                        # Task status will be running/migrating, update it once the
                        # VMs are in-sync.
                        task_status = list(results.keys())[0]
                        msg = "All VM(s) available in the migration task are 'InSync'"
                    else:
                        msg = (
                            "Status of all VM(s) available in the migration task is '%s'"
                            % list(results.keys())[0]
                        )
                    module.exit_json(
                        results=results,
                        status=task_status,
                        msg=msg,
                        sync_vms=sync_vms,
                        total_vms=total_objects,
                    )
                else:
                    module.exit_json(
                        msg="Status of the migration task is '%s'" % status,
                        status=status,
                    )
            else:
                module.fail_json(
                    msg="Couldn't find the task details.", status="Invalid"
                )

    elif module.params.get("state") == "absent":

        results = dict(
            changed=False,
            msg="Cohesity Migrate: This feature (absent) has not be implemented yet.",
            name=module.params.get("task_name"),
        )
    else:
        # => This error should never happen based on the set assigned to the parameter.
        # => However, in case, we should raise an appropriate error.
        module.fail_json(
            msg="Invalid State selected: {0}".format(module.params.get("state")),
            changed=False,
            status="Invalid",
        )

    module.exit_json(**results)


if __name__ == "__main__":
    main()
