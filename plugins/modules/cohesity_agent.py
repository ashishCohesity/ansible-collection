#!/usr/bin/python
# Copyright (c) 2022 Cohesity Inc

from __future__ import absolute_import, division, print_function

__metaclass__ = type

# GNU General Public License v3.0+ (see https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = """
---
author: "Naveena (@naveena-maplelabs)"
description:
  - "Ansible Module used to deploy or remove the Cohesity Physical Agent from supported Linux Machines."
  - "When executed in a playbook, the Cohesity Agent installation will be validated and the appropriate"
  - "state action will be applied.  The most recent version of the Cohesity Agent will be automatically"
  - "downloaded to the host."
module: cohesity_agent
options:
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
      - AD.domain.com/username
      - AD.domain.com/username@tenant
      - LOCAL/username@tenant
    type: str
  cohesity_password:
    aliases:
      - password
      - admin_pass
    description:
      - "Password belonging to the selected Username.  This parameter will not be logged."
    type: str
  create_user:
    default: true
    description:
      - "When enabled, will create a new user and group based on the values of I(service_user) and I(service_group)"
      - "This parameter does not apply for native installations."
    required: false
    type: bool
  download_location:
    description:
      - "Optional directory path to which the installer will be downloaded.  If not selected, then a temporary"
      - "directory will be created in the default System Temp Directory.  When choosing an alternate directory,"
      - "the directory and installer will not be deleted at the end of the execution."
    type: str
    default: ""
  download_uri:
    default: ""
    description:
      - "The download uri from where the installer can be downloaded"
    type: str
  file_based:
    default: false
    description:
      - "When enabled, will install the agent in non-LVM mode and support only file based backups."
    required: false
    type: bool
  host:
    default: ""
    description:
      - "Host name of the source."
    type: str
  native_package:
    default: false
    description:
      - "When enabled, native installer packages are used based on the operating system"
    type: bool
  operating_system:
    description:
      - "ansible_distribution from facts, this value is automatically populated. Not given by module user"
    type: str
    default: ""
  service_group:
    default: cohesityagent
    description:
      - "Group underwhich permissions will be configured for the Cohesity Agent configuration."
      - "This group must exist unless I(create_user=True) is also configured."
      - "This parameter doesn't apply for native installation."
    type: str
  service_user:
    default: cohesityagent
    description:
      - "Username underwhich the Cohesity Agent will be installed and run."
      - "This user must exist unless I(create_user=True) is also configured."
      - "This user must be an existing user for native installation."
    type: str
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - "Determines if the agent should be C(present) or C(absent) from the host"
    type: str
  upgrade:
    default: false
    description:
      - "If set to true and agent is already installed in the source, agent will be upgraded."
    required: false
    type: bool

  wait_minutes:
    default: 30
    description:
      - "Wait time for agent installation."
    required: false
    type: int
extends_documentation_fragment:
- cohesity.dataprotect.cohesity
short_description: "Management of Cohesity Physical Agent"
version_added: 1.2.0
"""

import os
import json
import time
import shutil

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_bytes
from ansible.module_utils.urls import open_url, urllib_error
from tempfile import mkdtemp

try:
    from ansible_collections.cohesity.dataprotect.plugins.module_utils.cohesity_utilities import (
        cohesity_common_argument_spec,
        raise__cohesity_exception__handler,
        REQUEST_TIMEOUT,
    )
    from ansible_collections.cohesity.dataprotect.plugins.module_utils.cohesity_auth import (
        get__cohesity_auth__token,
    )
except Exception:
    pass


EXAMPLES = """
# Install the current version of the agent on Linux
- cohesity_agent:
    server: cohesity.lab
    cohesity_admin: admin
    cohesity_password: password
    state: present

# Install the current version of the agent with custom User and Group
- cohesity_agent:
    server: cohesity.lab
    cohesity_admin: admin
    cohesity_password: password
    state: present
    service_user: cagent
    service_group: cagent
    create_user: True

# Removes the current installed agent from the host
- cohesity_agent:
    server: cohesity.lab
    cohesity_admin: admin
    cohesity_password: password
    state: absent

# Download the agent installer to a custom location.
- cohesity_agent:
    server: cohesity.lab
    cohesity_admin: admin
    cohesity_password: password
    download_location: /software/installers
    state: present

# Install the current version of the agent on Linux using native installers, the service user here should be an
# existing user
- cohesity_agent:
    server: cohesity.lab
    cohesity_admin: admin
    cohesity_password: password
    state: present
    service_user: cagent
    native_package: True

# Install the cohesity agent using native package downloaded from given URI. Here, the Cohesity cluster credentials are not required
- cohesity_agent:
    state: present
    service_user: cagent
    native_package: True
    download_uri: 'http://192.168.1.1/files/bin/installers/el-cohesity-agent-6.3-1.x86_64.rpm'

"""

RETURN = """
"""

SLEEP_TIME_SECONDS = 120
SECONDS_MINUTES_CONVERSION = 60


class InstallError(Exception):
    pass


def verify_dependencies():
    # => TODO:  Need to add package dependency checks for:
    # => wget, rsync, lsof, nfs-utils, lvm2
    pass

def check_agent(module, results):
    # Define paths for various agent scripts
    aix_agent_path = "/usr/local/cohesity/agent/aix_agent.sh"
    def_agent_path = "/etc/init.d/cohesity-agent"
    power_agent_path = "/opt/cohesity/java_agent/config/cohesity-java-agent"
    solaris_agent_path = "/usr/local/cohesity/agent/solaris_agent.sh"
    hpux_agent_path = "/usr/local/cohesity/agent/hpux_agent.sh"

    # Determine which agent path exists
    agent_path = (
        def_agent_path
        if os.path.exists(def_agent_path)
        else aix_agent_path
        if os.path.exists(aix_agent_path)
        else power_agent_path
        if os.path.exists(power_agent_path)
        else solaris_agent_path
        if os.path.exists(solaris_agent_path)
        else hpux_agent_path
        if os.path.exists(hpux_agent_path)
        else None
    )

    if agent_path:
        cmd = "%s version" % agent_path
        rc, out, err = module.run_command(cmd)
        split_out = out.split("\n")
        version = ""
        for v in split_out:
            if v.startswith("Version"):
                version = v.split(" ")[-1]
                break
        if version:
            results["version"] = version
        else:
            cmd = "rpm -q cohesity-agent"
            rc, out, err = module.run_command(cmd)
            split_out = out.split("\n")
            version = ""
            for v in split_out:
                if v.startswith("package cohesity-agent is not installed"):
                    version = None
                    break
                if v.startswith("cohesity-java-agent"):
                    version = v.split("-")[3]
                    break
                if v.startswith("cohesity-agent"):
                    version = v.split("-")[2]
                    break
            if version == "":
                results["version"] = "unknown"
            else:
                results["version"] = version
            results["check_agent"] = dict(stdout=out, stderr=err)
        return results
    elif os.path.exists("/etc/cohesity-agent"):
        cmd = "rpm -q cohesity-agent"
        rc, out, err = module.run_command(cmd)
        split_out = out.split("\n")
        version = ""
        for v in split_out:
            if v.startswith("package cohesity-agent is not installed"):
                version = None
                break
            if v.startswith("cohesity-java-agent"):
                version = v.split("-")[3]
                break
            if v.startswith("cohesity-agent"):
                version = v.split("-")[2]
                break
        if version == "":
            results["version"] = "unknown"
        else:
            results["version"] = version
        results["check_agent"] = dict(stdout=out, stderr=err)
        return results
    else:
        cmd = "ps -aux | grep crux/bin/linux_agent | grep -v python | awk '{print $2}'"
        rc, out, err = module.run_command(cmd, check_rc=True, use_unsafe_shell=True)
        if out:
            orphaned_agents = out.split("\n")
            for process in orphaned_agents:
                if process:
                    try:
                        cmd = "kill -9 {0}".format(process)
                    except BaseException:
                        cmd = "kill -9 %s" % (process)
                    rc, out, err = module.run_command(cmd)

                    if err:
                        pattern = "No such process"
                        if pattern in err:
                            pass
                        else:
                            results["changed"] = False
                            results["Failed"] = True
                            results["check_agent"] = dict(stdout=out, stderr=err)
                            results["process_id"] = process
                            module.fail_json(
                                msg="Failed to remove an orphaned Cohesity Agent service which is still running",
                                **results
                            )
                    else:
                        pass
            results["version"] = False
            return results
        else:
            results["version"] = False
            return results


def installation_failures(module, stdout, rc, message):
    # => The way that this installer works, we will not get back messages in stderr
    # => when a failure occurs.  For this reason, we need to jump through some hoops
    # => to extract the error messages.  The install will *Partially* complete even
    # => if certain dependencies are missing.
    # =>
    # => This block of code will first split the stdout into a List of strings that
    # => we will filter for any line which contains *Error:*.  Those lines will be
    # => returned to a new list *stderr* which will be formatted into a \n delimited
    # => string as the final step, we will raise a module failure to halt progress.
    stdout_lines = stdout.split("\n")

    # => Grab any Line that begins with Error:
    stderr = [k for k in stdout_lines if "Error:" in k]
    stderr = "\n".join(stderr)

    # => Grab any Line that begins with WARNING:
    stdwarn = [k for k in stdout_lines if "WARNING:" in k]
    stdwarn = "\n".join(stdwarn)
    module.fail_json(
        changed=False,
        msg=message,
        error=stderr,
        output=stdout,
        warn=stdwarn,
        exitcode=rc,
    )


def install_agent(module, installer, native):
    # => This command will run the self-extracting installer for the agent on machine and
    # => suppress opening a new window (nox11) and not show the extraction (noprogress) results
    # => which end up in stderr.
    #
    # => Note: Python 2.6 doesn't fully support the new string formatters, so this
    # => try..except will give us a clean backwards compatibility.

    # Check if sudo is available
    sudo_available = module.run_command("which sudo")[0] == 0

    # Create the user if create_user is true
    if module.params.get("create_user"):
        service_user = module.params.get("service_user", "cohesityagent")  # Default to 'cohesityagent' if not specified
        service_group = module.params.get("service_group", service_user)  # Default to user name if group not specified
        
        # Check if the user and group already exist
        user_exists = module.run_command("lsuser {}".format(service_user))
        group_exists = module.run_command("lsgroup {}".format(service_group))

        # Create the user and group if they do not exist
        if user_exists != 0:
            create_user_command = "mkuser {}".format(service_user)
            if module.params.get("operating_system") == "AIX":
                create_user_command = "mkuser {}".format(service_user)
            module.run_command(create_user_command)
        if group_exists != 0:
            create_group_command = "mkgroup {}".format(service_group)
            if module.params.get("operating_system") == "AIX":
                create_group_command = "mkgroup {}".format(service_group)
            module.run_command(create_group_command)


        if sudo_available:
            # Configure sudoers for the new user if sudo is available
            sudoers_entry = "{} ALL=(ALL) NOPASSWD:ALL\nDefaults:{} !requiretty".format(service_user, service_user)
            module.run_command('echo "{}" | sudo tee /etc/sudoers.d/{} > /dev/null'.format(sudoers_entry, service_user))
            module.run_command("sudo chmod 0440 /etc/sudoers.d/{}".format(service_user))


    if not native:
        install_opts = (
            "--create-user " + str(int(module.params.get("create_user"))) + " "
        )
        if module.params.get("service_user"):
            install_opts += "--service-user " + module.params.get("service_user") + " "
        if module.params.get("service_group"):
            install_opts += (
                "--service-group " + module.params.get("service_group") + " "
            )
        if module.params.get("file_based"):
            install_opts += "--skip-lvm-check "
        try:
            cmd = "{0}/setup.sh --install --yes {1}".format(installer, install_opts)
        except Exception:
            cmd = "%s/setup.sh --install --yes %s" % (installer, install_opts)
    else:
        try:
            if module.params.get("service_user"):
                user = module.params.get("service_user")
            if module.params.get("operating_system") == "Ubuntu":
                cmd = "sudo COHESITYUSER={0} dpkg -i {1}".format(user, installer)
            elif module.params.get("operating_system") in (
                "CentOS",
                "RedHat",
                "OracleLinux",
                "Rocky"
            ):
                cmd = "sudo COHESITYUSER={0} rpm -i {1}".format(user, installer)
            elif module.params.get("operating_system") == "AIX":
                if sudo_available:
                    cmd = "sudo COHESITYUSER={0} installp -ad {1} all".format(
                        user, installer
                    )
                else:
                    cmd = "su - root -c 'COHESITYUSER={0} installp -ad {1} all'".format(
                        user, installer
                    )
            elif module.params.get("operating_system") == "HP-UX":
                cmd = "swinstall -s {0} -x reinstall=true *".format(installer)
            elif "Solaris" in module.params.get("operating_system") :
              # Command for installing package on Solaris as root
                cmd = "su - root -c '/usr/sbin/pkgadd -a /root/insadmin -d {0} < /root/allinp'".format(installer)
            else:
                installation_failures(
                    module,
                    "",
                    "",
                    str(module.params.get("operating_system"))
                    + " isn't supported by cohesity ansible module",
                )
        except Exception:
            if module.params.get("operating_system") == "Ubuntu":
                cmd = "sudo COHESITYUSER=%s dpkg -i %s" % (user, installer)
            elif module.params.get("operating_system") in (
                "CentOS",
                "RedHat",
                "OracleLinux",
                "Rocky"
            ):
                cmd = "sudo COHESITYUSER=%s  rpm -i %s" % (user, installer)

    rc, stdout, stderr = module.run_command(cmd)

    # => Any return code other than 0 is considered a failure.
    if rc:
        installation_failures(
            module, stdout, rc, "Cohesity Agent is partially installed 1 " + cmd
        )
    return (True, "Successfully Installed the Cohesity agent")


def extract_agent(module, filename):
    # => This command will run the self-extracting installer in no execution mode
    #
    # => Note: Python 2.6 doesn't fully support the new string formatters, so this
    # => try..except will give us a clean backwards compatibility.
    directory = os.path.dirname(os.path.abspath(filename))
    target = directory + "/install_files"
    create_download_dir(module, target)
    try:
        cmd = "{0} --nox11 --noexec --target {1} ".format(filename, target)
    except Exception:
        cmd = "%s --nox11 --noexec --target %s " % (filename, target)

    rc, stdout, stderr = module.run_command(cmd)

    # => Any return code other than 0 is considered a failure.
    if rc:
        installation_failures(
            module, stdout, rc, "Cohesity Agent is partially installed 2"
        )
    return (True, "Successfully Installed the Cohesity agent", target)


def remove_agent(module, installer, native):
    # => This command will run the self-extracting installer for the agent on machine and
    # => suppress opening a new window (nox11) and not show the extraction (noprogress) results
    # => which end up in stderr.
    #
    # => Note: Python 2.6 doesn't fully support the new string formatters, so this
    # => try..except will give us a clean backwards compatibility.
    if not native:
        try:
            cmd = "{0}/setup.sh --full-uninstall --yes".format(installer)
        except Exception:
            cmd = "%s/setup.sh --full-uninstall --yes" % (installer)
        rc, out, err = module.run_command(cmd, cwd=installer)

        # => Any return code other than 0 is considered a failure.
        if rc:
            installation_failures(
                module, out, rc, "Cohesity Agent is partially installed 3"
            )
    else:
        if module.params.get("operating_system") == "AIX":
            cmd = "installp -u cohesity_agent.rte"
            rc, stdout, err = module.run_command(cmd)
            if rc:
                installation_failures(
                    module, stdout, rc, "Failed to uninstall cohesity agent"
                )
        elif module.params.get("operating_system") == "HP-UX":
            cmd = "swremove cohesity_agent"
            rc, stdout, err = module.run_command(cmd)
            if rc:
                installation_failures(
                    module, stdout, rc, "Failed to uninstall cohesity agent"
                )
        elif module.params.get("operating_system") == "Ubuntu":
            cmd = "sudo dpkg -P cohesity-agent"
            rc, stdout, stderr = module.run_command(cmd)
            if rc:
                installation_failures(
                    module, stdout, rc, "Failed to uninstall cohesity agent "
                )
        elif module.params.get("operating_system") in (
            "CentOS",
            "RedHat",
            "OracleLinux",
        ):
            cmd = "sudo rpm -e cohesity-agent"
            rc, stdout, stderr = module.run_command(cmd)
            if rc:
                installation_failures(
                    module, stdout, rc, "Failed to uninstall cohesity agent"
                )
            cmd = "sudo rm -rf /etc/cohesity-agent"
            rc, stdout, stderr = module.run_command(cmd)
            if rc:
                installation_failures(
                    module,
                    stdout,
                    rc,
                    "The cohesity agent is uninstalled but failed to remove /etc/cohesity-agent",
                )
        elif "Solaris" in module.params.get("operating_system") :
            # cmd = "su"
            # rc, stdout, stderr = module.run_command(cmd)
            # if rc:
            #     installation_failures(
            #         module,
            #         stdout,
            #         rc,

            #         "Failed to become superuser",
            #     )
            cmd = "su - root -c 'yes | /usr/sbin/pkgrm -v -a insadmin cohesity-agent'"
            # cmd = "printf " +'y\n'+ "  su - root -c '/usr/sbin/pkgrm -v -a \root\insadmin cohesity-agent'"
            rc, stdout, stderr = module.run_command(cmd)
            if rc:
                installation_failures(
                    module,
                    stdout,
                    rc,
                    "Failed to uninstall cohesity agent ",
                )

        else:
            installation_failures(
                module,
                "",
                "",
                str(module.params.get("operating_system"))
                + " is not supported by cohesity ansible module",
            )

    return (True, "Successfully Removed the Cohesity agent")


def create_download_dir(module, dir_path):
    # => Note: 2022-12-06
    # => Added this method to provide an alternate parameter to download the installer.
    # => This code was almost entirely pulled out of the Ansible File module.
    curpath = ""
    # => Determine if the download directory exists and if not then create it.
    for dirname in dir_path.strip("/").split("/"):
        curpath = "/".join([curpath, dirname])
        # Remove leading slash if we're creating a relative path
        if not os.path.isabs(dir_path):
            curpath = curpath.lstrip("/")
        b_curpath = to_bytes(curpath, errors="surrogate_or_strict")
        if not os.path.exists(b_curpath):
            try:
                os.mkdir(b_curpath)
            except OSError as ex:
                import errno

                # Possibly something else created the dir since the os.path.exists
                # check above. As long as it's a dir, we don't need to error
                # out.
                if not (ex.errno == errno.EEXIST and os.path.isdir(b_curpath)):
                    raise


def get_source_details(module, source_id):
    """
    Get protection source details
    :param module: object that holds parameters passed to the module
    :param source_id: protection source id
    :return:
    """
    server = module.params.get("cluster")
    validate_certs = module.params.get("validate_certs")
    token = get__cohesity_auth__token(module)
    try:
        if source_id:
            uri = (
                "https://"
                + server
                + "/irisservices/api/v1/public/protectionSources?id="
                + str(source_id)
            )
        else:
            uri = (
                "https://"
                + server
                + "/irisservices/api/v1/public/protectionSources?environments=kPhysical"
            )
        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer " + token,
            "user-agent": "cohesity-ansible/v1.2.0",
        }
        response = open_url(
            url=uri,
            headers=headers,
            validate_certs=validate_certs,
            method="GET",
            timeout=REQUEST_TIMEOUT,
        )
        response = json.loads(response.read())
        if source_id:
            nodes = response
        else:
            nodes = response[0]["nodes"]
        source_details = dict()
        for source in nodes:
            if source["protectionSource"]["name"] == module.params.get("host"):
                source_details["agent"] = source["protectionSource"][
                    "physicalProtectionSource"
                ]["agents"][0]
                source_details["id"] = source["protectionSource"]["id"]
        if not source_details:
            module.fail_json(changed=False, msg="Can't find the host on the cluster")
        return source_details
    except urllib_error.URLError as e:
        # => Capture and report any error messages.
        raise__cohesity_exception__handler(e.read(), module)
    except Exception as error:
        raise__cohesity_exception__handler(error, module)


def update_agent(module):
    """
    upgrades the agent on physical servers
    :param module: object that holds parameters passed to the module
    :return:
    """
    server = module.params.get("cluster")
    validate_certs = module.params.get("validate_certs")
    token = get__cohesity_auth__token(module)
    result = dict(changed=False, msg="", version="")
    try:
        source_details = get_source_details(module, None)
        if source_details["agent"]["upgradability"] == "kUpgradable":
            uri = (
                "https://"
                + server
                + "/irisservices/api/v1/public/physicalAgents/upgrade"
            )
            headers = {
                "Accept": "application/json",
                "Authorization": "Bearer " + token,
                "user-agent": "cohesity-ansible/v1.2.0",
            }
            payload = {"agentIds": [source_details["agent"]["id"]]}
            open_url(
                url=uri,
                data=json.dumps(payload),
                headers=headers,
                validate_certs=validate_certs,
                method="POST",
                timeout=REQUEST_TIMEOUT,
            )

            wait_time = module.params.get("wait_minutes")
            while wait_time > 0:
                poll_source_details = get_source_details(module, source_details["id"])
                if not poll_source_details:
                    result["changed"] = True
                    result["msg"] = (
                        "Update agent request is accepted but failed to check agent"
                        " status during upgrade wait time"
                    )
                    result["version"] = source_details["agent"]["version"]
                    module.exit_json(**result)
                elif poll_source_details["agent"].get("upgradeStatusMessage", ""):
                    module.fail_json(
                        changed=False,
                        msg="Failed to upgrade agent. "
                        + poll_source_details["agent"]["upgradeStatusMessage"],
                    )
                elif poll_source_details["agent"]["upgradeStatus"] == "kFinished":
                    result["changed"] = True
                    result["msg"] = "Successfully upgraded the agent"
                    result["version"] = poll_source_details["agent"]["version"]
                    module.exit_json(**result)
                time.sleep(SLEEP_TIME_SECONDS)
                wait_time = wait_time - (
                    SLEEP_TIME_SECONDS / SECONDS_MINUTES_CONVERSION
                )
            result["changed"] = True
            result["msg"] = (
                "The agent upgrade request is accepted."
                " The upgrade is not finished in the wait time"
            )
            result["version"] = source_details["agent"]["version"]
            module.exit_json(**result)
        elif source_details["agent"]["upgradability"] == "kCurrent":
            result["msg"] = "The host has the latest agent version"
            result["version"] = source_details["agent"]["version"]
            module.exit_json(**result)
        elif source_details["agent"]["upgradability"] == "kNonUpgradableAgentIsNewer":
            result["msg"] = (
                "The agent version running on the host is newer"
                " than the agent version on the cluster"
            )
            result["version"] = source_details["agent"]["version"]
            module.exit_json(**result)
        elif source_details["agent"]["upgradability"] == "kNonUpgradableAgentIsOld":
            module.fail_json(
                changed=False,
                msg="The agent version running on the host is too old to support upgrades",
            )
        else:
            module.fail_json(
                changed=False,
                msg="Can't upgrade the agent due to unknown or invalid"
                " agent version running on the host",
            )
    except urllib_error.URLError as e:
        # => Capture and report any error messages.
        raise__cohesity_exception__handler(e.read(), module)
    except Exception as error:
        raise__cohesity_exception__handler(error, module)

def main():
    # => Load the default arguments including those specific to the Cohesity Agent.
    argument_spec = cohesity_common_argument_spec()
    argument_spec.update(
        dict(
            state=dict(choices=["present", "absent"], default="present", type="str"),
            download_location=dict(default="/"),
            service_user=dict(default="cohesityagent"),
            service_group=dict(default="cohesityagent"),
            create_user=dict(default=True, type="bool"),
            file_based=dict(default=False, type="bool"),
            native_package=dict(default=False, type="bool"),
            operating_system=dict(default="", type="str"),
            host=dict(type="str", default=""),
            upgrade=dict(type="bool", default=False),
            wait_minutes=dict(type="int", default=30),
            installer_path=dict(type="str", default=""),
        )
    )

    # => Create a new module object
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)
    results = dict(changed=False, version=False, state=module.params.get("state"))

    # Agent installation for AIX operating system is done using native package.
    if module.params.get("operating_system") == "AIX":
        module.params["native_package"] = True

    success = True
    try:
        if module.check_mode:
            results = check_agent(module, results)
            check_mode_results = dict(
                changed=False,
                msg="Check Mode: Agent is Currently not Installed",
                version="",
            )
            if module.params.get("state") == "present":
                if results["version"]:
                    check_mode_results[
                        "msg"
                    ] = "Check Mode: Agent is currently installed.  No changes"
                else:
                    check_mode_results["msg"] = (
                        "Check Mode: Agent is currently not installed."
                        + " This action would install the Agent."
                    )
                    check_mode_results["version"] = results["version"]
            else:
                if results["version"]:
                    check_mode_results[
                        "msg"
                    ] = "Check Mode: Agent is currently installed.  This action would uninstall the Agent."
                    check_mode_results["version"] = results["version"]
                else:
                    check_mode_results[
                        "msg"
                    ] = "Check Mode: Agent is currently not installed.  No changes."
            module.exit_json(**check_mode_results)

        elif module.params.get("state") == "present" and not module.params.get(
            "upgrade"
        ):
            # => Check if the Cohesity Agent is currently installed and only trigger the install
            # => if the agent does not exist.
            results = check_agent(module, results)

            if not results["version"]:
                if not module.params.get("native_package"):
                    results["filename"] = module.params.get("installer_path")
                    results["changed"], results["message"], results["installer"] = extract_agent(module, results["filename"])
                    results["changed"], results["message"] = install_agent(
                        module, results["installer"], False
                    )
                    results = check_agent(module, results)
                else:
                    results["filename"] = module.params.get("installer_path")
                    results["changed"], results["message"] = install_agent(
                        module, results["filename"], True
                    )
                    results = check_agent(module, results)
            elif results["version"] == "unknown":
                # => There is a problem that we should invesitgate.
                module.fail_json(msg="Cohesity Agent is partially installed", **results)
            else:
                # => If we received a valid version then the assumption will be
                # => that the Agent is installed.  We should simply pass it foward
                # => and act like things are normal.
                pass
        elif module.params.get("state") == "present" and module.params.get("upgrade"):
            if not module.params.get("host"):
                module.fail_json(
                    changed=False,
                    msg="The host parameter is required for agent upgrades",
                )
            update_agent(module)
        elif module.params.get("state") == "absent":
            # => Check if the Cohesity Agent is currently installed and only trigger the uninstall
            # => if the agent exists.
            results = check_agent(module, results)

            # => If anything is returned, we should remove the agent.  We also don't care if there
            # => is any output from the check so we will pop that out of the results to clean up
            # => our return data.
            if results["version"]:
                if not module.params.get("native_package"):
                    results.pop("check_agent", None)
                    results["filename"] = module.params.get("installer_path")
                    results["changed"], results["message"], results["installer"] = extract_agent(module, results["filename"])
                    results["changed"], results["message"] = remove_agent(
                        module, results["installer"], False
                    )
                else:
                    results["changed"], results["message"] = remove_agent(
                        module, "", True
                    )
        else:
            # => This error should never happen based on the set assigned to the parameter.
            # => However, in case, we should raise an appropriate error.
            module.fail_json(
                msg="Invalid State selected: {0}".format(module.params.get("state")),
                changed=False,
            )
    except Exception as error:
        # => The exception handler should still trigger but just in case, let's set this
        # => variable 'success' to be False.
        success = False

        # => Call the proper error handler.
        msg = "Unexpected error caused while managing the Cohesity Linux Agent."
        raise__cohesity_exception__handler(error, module, msg)

    

    if success:
        # -> Return Ansible JSON
        module.exit_json(**results)
    else:
        module.fail_json(msg="Cohesity Agent Failed", **results)


if __name__ == "__main__":
    main()
