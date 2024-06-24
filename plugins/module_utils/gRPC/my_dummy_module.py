# my_dummy_module.py

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cohesity.dataprotect.plugins.module_utils.basic import generate_greeting

def run_module():
    module_args = dict(
        name=dict(type="str", required=True)
    )

    result = dict(
        changed=False,
        original_message="",
        message=""
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    name = module.params["name"]
    result["original_message"] = name
    result["message"] = generate_greeting(name)

    if module.check_mode:
        module.exit_json(**result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == "__main__":
    main()
