import os
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cohesity.dataprotect.plugins.module_utils.my_greeting_module import generate_greeting

def get_environment_variables():
    env_vars = []
    for key, value in os.environ.items():
        env_vars.append((str(key), str(value)))
    return env_vars

def run_module():
    module_args = dict(name=dict(type="str", required=True))

    result = dict(
        changed=False,
        original_message="",
        message="",
        Length=0,  # Placeholder for the length of environment variables (to be populated later)
        Paths=[]   # Placeholder for the list of environment variables (to be populated later)
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    name = module.params["name"]
    result["original_message"] = name
    result["message"] = generate_greeting(name)

    # # Fetch environment variables and populate result dictionary
    # env_vars = get_environment_variables()
    # result["Length"] = len(env_vars)
    # result["Paths"] = env_vars

    if module.check_mode:
        module.exit_json(**result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == "__main__":
    main()
