from magneto.connectors.outlook import outlook_param_pb2 as _outlook_param_pb2
from magneto.connectors.ms_graph import graph_params_pb2 as _graph_params_pb2
from magneto.connectors.sharepoint import sharepoint_params_pb2 as _sharepoint_params_pb2
from magneto.base import magneto_pb2 as _magneto_pb2
from magneto.base import env_params_pb2 as _env_params_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class O365EmulatorItemInfo(_message.Message):
    __slots__ = ("domain", "smtp_address", "user_id", "folder_id", "item_id", "item_size", "drive_id", "file_id", "file_size", "path", "site_id", "site_drive_id", "teams_id", "group_id", "root_public_folder", "parent_public_folder_id", "channel_id", "sec_group_id", "site_list_id")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    SMTP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_SIZE_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    TEAMS_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ROOT_PUBLIC_FOLDER_FIELD_NUMBER: _ClassVar[int]
    PARENT_PUBLIC_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    SEC_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    domain: str
    smtp_address: str
    user_id: int
    folder_id: int
    item_id: int
    item_size: int
    drive_id: int
    file_id: int
    file_size: int
    path: str
    site_id: int
    site_drive_id: int
    teams_id: int
    group_id: int
    root_public_folder: bool
    parent_public_folder_id: int
    channel_id: int
    sec_group_id: int
    site_list_id: int
    def __init__(self, domain: _Optional[str] = ..., smtp_address: _Optional[str] = ..., user_id: _Optional[int] = ..., folder_id: _Optional[int] = ..., item_id: _Optional[int] = ..., item_size: _Optional[int] = ..., drive_id: _Optional[int] = ..., file_id: _Optional[int] = ..., file_size: _Optional[int] = ..., path: _Optional[str] = ..., site_id: _Optional[int] = ..., site_drive_id: _Optional[int] = ..., teams_id: _Optional[int] = ..., group_id: _Optional[int] = ..., root_public_folder: bool = ..., parent_public_folder_id: _Optional[int] = ..., channel_id: _Optional[int] = ..., sec_group_id: _Optional[int] = ..., site_list_id: _Optional[int] = ...) -> None: ...

class O365EmulatorGflags(_message.Message):
    __slots__ = ("num_create_users", "change_user_rate", "mailbox_max_folders_range", "mailbox_max_items_range", "mailbox_num_folder_create", "mailbox_folder_update_rate", "mailbox_folder_delete_rate", "mailbox_stop_folder_update_after_max_limit", "mailbox_num_item_create", "mailbox_item_update_rate", "mailbox_item_delete_rate", "mailbox_stop_item_update_after_max_limit", "num_drives_per_user", "drive_max_items_in_delta_call", "drive_branching_factor", "drive_max_folder_depth", "drive_max_files", "drive_incr_delta_percent", "drive_incr_create_delta_percent", "drive_incr_delete_delta_percent", "drive_max_files_in_folder", "drive_max_random_string_length", "create_sites", "num_create_sites", "num_create_site_drives", "create_teams", "num_create_teams", "num_create_teams_channel", "create_groups", "num_create_groups", "create_public_folders", "num_create_root_publicfolders", "num_create_publicfolders", "change_public_folders_rate", "change_sites_rate", "change_groups_rate", "change_teams_rate", "mailbox_min_item_size_bytes", "mailbox_max_item_size_bytes", "drive_min_file_size_bytes", "drive_max_file_size_bytes", "mailbox_folder_create_rate", "mailbox_item_create_rate", "random_number_generator_seed", "drive_change_e_tag_on_update", "drive_change_name_on_update", "drive_item_min_permissions", "drive_item_max_permissions", "drive_incr_update_delta_percent", "o365_emulator_varz_dump_filepath", "o365_emulator_varz_dump_period_secs", "site_drive_max_files", "site_drive_incr_delta_percent", "site_drive_incr_create_delta_percent", "site_drive_incr_update_delta_percent", "site_drive_incr_delete_delta_percent", "site_drive_max_files_in_folder", "site_drive_min_file_size_bytes", "site_drive_max_file_size_bytes", "team_channel_site_drive_max_files", "team_channel_site_drive_incr_delta_percent", "team_channel_site_drive_incr_create_delta_percent", "team_channel_site_drive_incr_update_delta_percent", "team_channel_site_drive_incr_delete_delta_percent", "team_channel_site_drive_max_files_in_folder", "team_channel_site_drive_min_file_size_bytes", "team_channel_site_drive_max_file_size_bytes", "team_group_site_drive_max_files", "team_group_site_drive_incr_delta_percent", "team_group_site_drive_incr_create_delta_percent", "team_group_site_drive_incr_update_delta_percent", "team_group_site_drive_incr_delete_delta_percent", "team_group_site_drive_max_files_in_folder", "team_group_site_drive_min_file_size_bytes", "team_group_site_drive_max_file_size_bytes", "group_site_drive_max_files", "group_site_drive_incr_delta_percent", "group_site_drive_incr_create_delta_percent", "group_site_drive_incr_update_delta_percent", "group_site_drive_incr_delete_delta_percent", "group_site_drive_max_files_in_folder", "group_site_drive_min_file_size_bytes", "group_site_drive_max_file_size_bytes", "group_mailbox_min_item_size_bytes", "group_mailbox_max_item_size_bytes", "num_group_initial_members", "num_group_initial_owners", "num_group_new_members", "num_group_new_owners", "num_group_remove_members", "num_group_remove_owners", "generate_random_string_with_lcg", "use_variable_distribution_for_mailbox", "normalize_mailbox_size", "mailbox_initial_folders_create_min", "mailbox_initial_folders_create_max", "mailbox_initial_items_create_min", "mailbox_initial_items_create_max", "custom_rules_mailbox_entity_distribution", "o365_emulator_run_recovery_verification_mode", "create_security_groups", "num_create_sec_groups", "sec_group_members_distribution", "create_lists", "num_create_lists", "num_create_list_items")
    NUM_CREATE_USERS_FIELD_NUMBER: _ClassVar[int]
    CHANGE_USER_RATE_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_MAX_FOLDERS_RANGE_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_MAX_ITEMS_RANGE_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_NUM_FOLDER_CREATE_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_FOLDER_UPDATE_RATE_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_FOLDER_DELETE_RATE_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_STOP_FOLDER_UPDATE_AFTER_MAX_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_NUM_ITEM_CREATE_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_ITEM_UPDATE_RATE_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_ITEM_DELETE_RATE_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_STOP_ITEM_UPDATE_AFTER_MAX_LIMIT_FIELD_NUMBER: _ClassVar[int]
    NUM_DRIVES_PER_USER_FIELD_NUMBER: _ClassVar[int]
    DRIVE_MAX_ITEMS_IN_DELTA_CALL_FIELD_NUMBER: _ClassVar[int]
    DRIVE_BRANCHING_FACTOR_FIELD_NUMBER: _ClassVar[int]
    DRIVE_MAX_FOLDER_DEPTH_FIELD_NUMBER: _ClassVar[int]
    DRIVE_MAX_FILES_FIELD_NUMBER: _ClassVar[int]
    DRIVE_INCR_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    DRIVE_INCR_CREATE_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    DRIVE_INCR_DELETE_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    DRIVE_MAX_FILES_IN_FOLDER_FIELD_NUMBER: _ClassVar[int]
    DRIVE_MAX_RANDOM_STRING_LENGTH_FIELD_NUMBER: _ClassVar[int]
    CREATE_SITES_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATE_SITES_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATE_SITE_DRIVES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TEAMS_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATE_TEAMS_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATE_TEAMS_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CREATE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    CREATE_PUBLIC_FOLDERS_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATE_ROOT_PUBLICFOLDERS_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATE_PUBLICFOLDERS_FIELD_NUMBER: _ClassVar[int]
    CHANGE_PUBLIC_FOLDERS_RATE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_SITES_RATE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_GROUPS_RATE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TEAMS_RATE_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_MIN_ITEM_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_MAX_ITEM_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DRIVE_MIN_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    DRIVE_MAX_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_FOLDER_CREATE_RATE_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_ITEM_CREATE_RATE_FIELD_NUMBER: _ClassVar[int]
    RANDOM_NUMBER_GENERATOR_SEED_FIELD_NUMBER: _ClassVar[int]
    DRIVE_CHANGE_E_TAG_ON_UPDATE_FIELD_NUMBER: _ClassVar[int]
    DRIVE_CHANGE_NAME_ON_UPDATE_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ITEM_MIN_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ITEM_MAX_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    DRIVE_INCR_UPDATE_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    O365_EMULATOR_VARZ_DUMP_FILEPATH_FIELD_NUMBER: _ClassVar[int]
    O365_EMULATOR_VARZ_DUMP_PERIOD_SECS_FIELD_NUMBER: _ClassVar[int]
    SITE_DRIVE_MAX_FILES_FIELD_NUMBER: _ClassVar[int]
    SITE_DRIVE_INCR_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    SITE_DRIVE_INCR_CREATE_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    SITE_DRIVE_INCR_UPDATE_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    SITE_DRIVE_INCR_DELETE_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    SITE_DRIVE_MAX_FILES_IN_FOLDER_FIELD_NUMBER: _ClassVar[int]
    SITE_DRIVE_MIN_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SITE_DRIVE_MAX_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TEAM_CHANNEL_SITE_DRIVE_MAX_FILES_FIELD_NUMBER: _ClassVar[int]
    TEAM_CHANNEL_SITE_DRIVE_INCR_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    TEAM_CHANNEL_SITE_DRIVE_INCR_CREATE_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    TEAM_CHANNEL_SITE_DRIVE_INCR_UPDATE_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    TEAM_CHANNEL_SITE_DRIVE_INCR_DELETE_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    TEAM_CHANNEL_SITE_DRIVE_MAX_FILES_IN_FOLDER_FIELD_NUMBER: _ClassVar[int]
    TEAM_CHANNEL_SITE_DRIVE_MIN_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TEAM_CHANNEL_SITE_DRIVE_MAX_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TEAM_GROUP_SITE_DRIVE_MAX_FILES_FIELD_NUMBER: _ClassVar[int]
    TEAM_GROUP_SITE_DRIVE_INCR_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    TEAM_GROUP_SITE_DRIVE_INCR_CREATE_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    TEAM_GROUP_SITE_DRIVE_INCR_UPDATE_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    TEAM_GROUP_SITE_DRIVE_INCR_DELETE_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    TEAM_GROUP_SITE_DRIVE_MAX_FILES_IN_FOLDER_FIELD_NUMBER: _ClassVar[int]
    TEAM_GROUP_SITE_DRIVE_MIN_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    TEAM_GROUP_SITE_DRIVE_MAX_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    GROUP_SITE_DRIVE_MAX_FILES_FIELD_NUMBER: _ClassVar[int]
    GROUP_SITE_DRIVE_INCR_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    GROUP_SITE_DRIVE_INCR_CREATE_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    GROUP_SITE_DRIVE_INCR_UPDATE_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    GROUP_SITE_DRIVE_INCR_DELETE_DELTA_PERCENT_FIELD_NUMBER: _ClassVar[int]
    GROUP_SITE_DRIVE_MAX_FILES_IN_FOLDER_FIELD_NUMBER: _ClassVar[int]
    GROUP_SITE_DRIVE_MIN_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    GROUP_SITE_DRIVE_MAX_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    GROUP_MAILBOX_MIN_ITEM_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    GROUP_MAILBOX_MAX_ITEM_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    NUM_GROUP_INITIAL_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    NUM_GROUP_INITIAL_OWNERS_FIELD_NUMBER: _ClassVar[int]
    NUM_GROUP_NEW_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    NUM_GROUP_NEW_OWNERS_FIELD_NUMBER: _ClassVar[int]
    NUM_GROUP_REMOVE_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    NUM_GROUP_REMOVE_OWNERS_FIELD_NUMBER: _ClassVar[int]
    GENERATE_RANDOM_STRING_WITH_LCG_FIELD_NUMBER: _ClassVar[int]
    USE_VARIABLE_DISTRIBUTION_FOR_MAILBOX_FIELD_NUMBER: _ClassVar[int]
    NORMALIZE_MAILBOX_SIZE_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_INITIAL_FOLDERS_CREATE_MIN_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_INITIAL_FOLDERS_CREATE_MAX_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_INITIAL_ITEMS_CREATE_MIN_FIELD_NUMBER: _ClassVar[int]
    MAILBOX_INITIAL_ITEMS_CREATE_MAX_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_RULES_MAILBOX_ENTITY_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    O365_EMULATOR_RUN_RECOVERY_VERIFICATION_MODE_FIELD_NUMBER: _ClassVar[int]
    CREATE_SECURITY_GROUPS_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATE_SEC_GROUPS_FIELD_NUMBER: _ClassVar[int]
    SEC_GROUP_MEMBERS_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_LISTS_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATE_LISTS_FIELD_NUMBER: _ClassVar[int]
    NUM_CREATE_LIST_ITEMS_FIELD_NUMBER: _ClassVar[int]
    num_create_users: int
    change_user_rate: int
    mailbox_max_folders_range: int
    mailbox_max_items_range: int
    mailbox_num_folder_create: int
    mailbox_folder_update_rate: int
    mailbox_folder_delete_rate: int
    mailbox_stop_folder_update_after_max_limit: bool
    mailbox_num_item_create: int
    mailbox_item_update_rate: int
    mailbox_item_delete_rate: int
    mailbox_stop_item_update_after_max_limit: bool
    num_drives_per_user: int
    drive_max_items_in_delta_call: int
    drive_branching_factor: int
    drive_max_folder_depth: int
    drive_max_files: int
    drive_incr_delta_percent: int
    drive_incr_create_delta_percent: int
    drive_incr_delete_delta_percent: int
    drive_max_files_in_folder: int
    drive_max_random_string_length: int
    create_sites: bool
    num_create_sites: int
    num_create_site_drives: int
    create_teams: bool
    num_create_teams: int
    num_create_teams_channel: int
    create_groups: bool
    num_create_groups: int
    create_public_folders: bool
    num_create_root_publicfolders: int
    num_create_publicfolders: int
    change_public_folders_rate: int
    change_sites_rate: int
    change_groups_rate: int
    change_teams_rate: int
    mailbox_min_item_size_bytes: int
    mailbox_max_item_size_bytes: int
    drive_min_file_size_bytes: int
    drive_max_file_size_bytes: int
    mailbox_folder_create_rate: int
    mailbox_item_create_rate: int
    random_number_generator_seed: int
    drive_change_e_tag_on_update: bool
    drive_change_name_on_update: bool
    drive_item_min_permissions: int
    drive_item_max_permissions: int
    drive_incr_update_delta_percent: int
    o365_emulator_varz_dump_filepath: str
    o365_emulator_varz_dump_period_secs: int
    site_drive_max_files: int
    site_drive_incr_delta_percent: int
    site_drive_incr_create_delta_percent: int
    site_drive_incr_update_delta_percent: int
    site_drive_incr_delete_delta_percent: int
    site_drive_max_files_in_folder: int
    site_drive_min_file_size_bytes: int
    site_drive_max_file_size_bytes: int
    team_channel_site_drive_max_files: int
    team_channel_site_drive_incr_delta_percent: int
    team_channel_site_drive_incr_create_delta_percent: int
    team_channel_site_drive_incr_update_delta_percent: int
    team_channel_site_drive_incr_delete_delta_percent: int
    team_channel_site_drive_max_files_in_folder: int
    team_channel_site_drive_min_file_size_bytes: int
    team_channel_site_drive_max_file_size_bytes: int
    team_group_site_drive_max_files: int
    team_group_site_drive_incr_delta_percent: int
    team_group_site_drive_incr_create_delta_percent: int
    team_group_site_drive_incr_update_delta_percent: int
    team_group_site_drive_incr_delete_delta_percent: int
    team_group_site_drive_max_files_in_folder: int
    team_group_site_drive_min_file_size_bytes: int
    team_group_site_drive_max_file_size_bytes: int
    group_site_drive_max_files: int
    group_site_drive_incr_delta_percent: int
    group_site_drive_incr_create_delta_percent: int
    group_site_drive_incr_update_delta_percent: int
    group_site_drive_incr_delete_delta_percent: int
    group_site_drive_max_files_in_folder: int
    group_site_drive_min_file_size_bytes: int
    group_site_drive_max_file_size_bytes: int
    group_mailbox_min_item_size_bytes: int
    group_mailbox_max_item_size_bytes: int
    num_group_initial_members: int
    num_group_initial_owners: int
    num_group_new_members: int
    num_group_new_owners: int
    num_group_remove_members: int
    num_group_remove_owners: int
    generate_random_string_with_lcg: bool
    use_variable_distribution_for_mailbox: bool
    normalize_mailbox_size: bool
    mailbox_initial_folders_create_min: int
    mailbox_initial_folders_create_max: int
    mailbox_initial_items_create_min: int
    mailbox_initial_items_create_max: int
    custom_rules_mailbox_entity_distribution: str
    o365_emulator_run_recovery_verification_mode: bool
    create_security_groups: bool
    num_create_sec_groups: int
    sec_group_members_distribution: str
    create_lists: bool
    num_create_lists: int
    num_create_list_items: int
    def __init__(self, num_create_users: _Optional[int] = ..., change_user_rate: _Optional[int] = ..., mailbox_max_folders_range: _Optional[int] = ..., mailbox_max_items_range: _Optional[int] = ..., mailbox_num_folder_create: _Optional[int] = ..., mailbox_folder_update_rate: _Optional[int] = ..., mailbox_folder_delete_rate: _Optional[int] = ..., mailbox_stop_folder_update_after_max_limit: bool = ..., mailbox_num_item_create: _Optional[int] = ..., mailbox_item_update_rate: _Optional[int] = ..., mailbox_item_delete_rate: _Optional[int] = ..., mailbox_stop_item_update_after_max_limit: bool = ..., num_drives_per_user: _Optional[int] = ..., drive_max_items_in_delta_call: _Optional[int] = ..., drive_branching_factor: _Optional[int] = ..., drive_max_folder_depth: _Optional[int] = ..., drive_max_files: _Optional[int] = ..., drive_incr_delta_percent: _Optional[int] = ..., drive_incr_create_delta_percent: _Optional[int] = ..., drive_incr_delete_delta_percent: _Optional[int] = ..., drive_max_files_in_folder: _Optional[int] = ..., drive_max_random_string_length: _Optional[int] = ..., create_sites: bool = ..., num_create_sites: _Optional[int] = ..., num_create_site_drives: _Optional[int] = ..., create_teams: bool = ..., num_create_teams: _Optional[int] = ..., num_create_teams_channel: _Optional[int] = ..., create_groups: bool = ..., num_create_groups: _Optional[int] = ..., create_public_folders: bool = ..., num_create_root_publicfolders: _Optional[int] = ..., num_create_publicfolders: _Optional[int] = ..., change_public_folders_rate: _Optional[int] = ..., change_sites_rate: _Optional[int] = ..., change_groups_rate: _Optional[int] = ..., change_teams_rate: _Optional[int] = ..., mailbox_min_item_size_bytes: _Optional[int] = ..., mailbox_max_item_size_bytes: _Optional[int] = ..., drive_min_file_size_bytes: _Optional[int] = ..., drive_max_file_size_bytes: _Optional[int] = ..., mailbox_folder_create_rate: _Optional[int] = ..., mailbox_item_create_rate: _Optional[int] = ..., random_number_generator_seed: _Optional[int] = ..., drive_change_e_tag_on_update: bool = ..., drive_change_name_on_update: bool = ..., drive_item_min_permissions: _Optional[int] = ..., drive_item_max_permissions: _Optional[int] = ..., drive_incr_update_delta_percent: _Optional[int] = ..., o365_emulator_varz_dump_filepath: _Optional[str] = ..., o365_emulator_varz_dump_period_secs: _Optional[int] = ..., site_drive_max_files: _Optional[int] = ..., site_drive_incr_delta_percent: _Optional[int] = ..., site_drive_incr_create_delta_percent: _Optional[int] = ..., site_drive_incr_update_delta_percent: _Optional[int] = ..., site_drive_incr_delete_delta_percent: _Optional[int] = ..., site_drive_max_files_in_folder: _Optional[int] = ..., site_drive_min_file_size_bytes: _Optional[int] = ..., site_drive_max_file_size_bytes: _Optional[int] = ..., team_channel_site_drive_max_files: _Optional[int] = ..., team_channel_site_drive_incr_delta_percent: _Optional[int] = ..., team_channel_site_drive_incr_create_delta_percent: _Optional[int] = ..., team_channel_site_drive_incr_update_delta_percent: _Optional[int] = ..., team_channel_site_drive_incr_delete_delta_percent: _Optional[int] = ..., team_channel_site_drive_max_files_in_folder: _Optional[int] = ..., team_channel_site_drive_min_file_size_bytes: _Optional[int] = ..., team_channel_site_drive_max_file_size_bytes: _Optional[int] = ..., team_group_site_drive_max_files: _Optional[int] = ..., team_group_site_drive_incr_delta_percent: _Optional[int] = ..., team_group_site_drive_incr_create_delta_percent: _Optional[int] = ..., team_group_site_drive_incr_update_delta_percent: _Optional[int] = ..., team_group_site_drive_incr_delete_delta_percent: _Optional[int] = ..., team_group_site_drive_max_files_in_folder: _Optional[int] = ..., team_group_site_drive_min_file_size_bytes: _Optional[int] = ..., team_group_site_drive_max_file_size_bytes: _Optional[int] = ..., group_site_drive_max_files: _Optional[int] = ..., group_site_drive_incr_delta_percent: _Optional[int] = ..., group_site_drive_incr_create_delta_percent: _Optional[int] = ..., group_site_drive_incr_update_delta_percent: _Optional[int] = ..., group_site_drive_incr_delete_delta_percent: _Optional[int] = ..., group_site_drive_max_files_in_folder: _Optional[int] = ..., group_site_drive_min_file_size_bytes: _Optional[int] = ..., group_site_drive_max_file_size_bytes: _Optional[int] = ..., group_mailbox_min_item_size_bytes: _Optional[int] = ..., group_mailbox_max_item_size_bytes: _Optional[int] = ..., num_group_initial_members: _Optional[int] = ..., num_group_initial_owners: _Optional[int] = ..., num_group_new_members: _Optional[int] = ..., num_group_new_owners: _Optional[int] = ..., num_group_remove_members: _Optional[int] = ..., num_group_remove_owners: _Optional[int] = ..., generate_random_string_with_lcg: bool = ..., use_variable_distribution_for_mailbox: bool = ..., normalize_mailbox_size: bool = ..., mailbox_initial_folders_create_min: _Optional[int] = ..., mailbox_initial_folders_create_max: _Optional[int] = ..., mailbox_initial_items_create_min: _Optional[int] = ..., mailbox_initial_items_create_max: _Optional[int] = ..., custom_rules_mailbox_entity_distribution: _Optional[str] = ..., o365_emulator_run_recovery_verification_mode: bool = ..., create_security_groups: bool = ..., num_create_sec_groups: _Optional[int] = ..., sec_group_members_distribution: _Optional[str] = ..., create_lists: bool = ..., num_create_lists: _Optional[int] = ..., num_create_list_items: _Optional[int] = ...) -> None: ...

class O365EmulatorEntityInfo(_message.Message):
    __slots__ = ("users_start_idx", "public_folders_start_idx", "sites_start_idx", "groups_start_idx", "teams_start_idx")
    USERS_START_IDX_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FOLDERS_START_IDX_FIELD_NUMBER: _ClassVar[int]
    SITES_START_IDX_FIELD_NUMBER: _ClassVar[int]
    GROUPS_START_IDX_FIELD_NUMBER: _ClassVar[int]
    TEAMS_START_IDX_FIELD_NUMBER: _ClassVar[int]
    users_start_idx: int
    public_folders_start_idx: int
    sites_start_idx: int
    groups_start_idx: int
    teams_start_idx: int
    def __init__(self, users_start_idx: _Optional[int] = ..., public_folders_start_idx: _Optional[int] = ..., sites_start_idx: _Optional[int] = ..., groups_start_idx: _Optional[int] = ..., teams_start_idx: _Optional[int] = ...) -> None: ...

class O365EmulatorCurrentFolderIds(_message.Message):
    __slots__ = ("id_vec", "run_id")
    ID_VEC_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    id_vec: _containers.RepeatedScalarFieldContainer[int]
    run_id: int
    def __init__(self, id_vec: _Optional[_Iterable[int]] = ..., run_id: _Optional[int] = ...) -> None: ...

class O365EmulatorCurrentGroupInfo(_message.Message):
    __slots__ = ("members_idx_vec", "owners_idx_vec")
    MEMBERS_IDX_VEC_FIELD_NUMBER: _ClassVar[int]
    OWNERS_IDX_VEC_FIELD_NUMBER: _ClassVar[int]
    members_idx_vec: _containers.RepeatedScalarFieldContainer[int]
    owners_idx_vec: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, members_idx_vec: _Optional[_Iterable[int]] = ..., owners_idx_vec: _Optional[_Iterable[int]] = ...) -> None: ...

class O365EmulatorSyncState(_message.Message):
    __slots__ = ("created", "deleted", "updated", "folder_path", "is_processed")
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    IS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    created: int
    deleted: int
    updated: int
    folder_path: str
    is_processed: bool
    def __init__(self, created: _Optional[int] = ..., deleted: _Optional[int] = ..., updated: _Optional[int] = ..., folder_path: _Optional[str] = ..., is_processed: bool = ...) -> None: ...

class O365EmulatorDeltaLink(_message.Message):
    __slots__ = ("is_fullbackup", "delta_state", "folder_state", "run_id")
    IS_FULLBACKUP_FIELD_NUMBER: _ClassVar[int]
    DELTA_STATE_FIELD_NUMBER: _ClassVar[int]
    FOLDER_STATE_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    is_fullbackup: bool
    delta_state: O365EmulatorSyncState
    folder_state: _containers.RepeatedCompositeFieldContainer[O365EmulatorSyncState]
    run_id: int
    def __init__(self, is_fullbackup: bool = ..., delta_state: _Optional[_Union[O365EmulatorSyncState, _Mapping]] = ..., folder_state: _Optional[_Iterable[_Union[O365EmulatorSyncState, _Mapping]]] = ..., run_id: _Optional[int] = ...) -> None: ...

class O365EmulatorGetMailboxListArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _outlook_param_pb2.GetMailboxListArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_outlook_param_pb2.GetMailboxListArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorValidateUserCredentialsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _outlook_param_pb2.ValidateUserCredentialsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_outlook_param_pb2.ValidateUserCredentialsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetOutlookHierarchyArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _outlook_param_pb2.GetOutlookHierarchyArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_outlook_param_pb2.GetOutlookHierarchyArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetFolderHierarchyChangesArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _outlook_param_pb2.GetFolderHierarchyChangesArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_outlook_param_pb2.GetFolderHierarchyChangesArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetMultipleFolderHierarchyChangesArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _outlook_param_pb2.GetMultipleFolderHierarchyChangesArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_outlook_param_pb2.GetMultipleFolderHierarchyChangesArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetFolderChangesArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _outlook_param_pb2.GetFolderChangesArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_outlook_param_pb2.GetFolderChangesArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetItemsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _outlook_param_pb2.GetItemsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_outlook_param_pb2.GetItemsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetItemMetadataArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _outlook_param_pb2.GetItemMetadataArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_outlook_param_pb2.GetItemMetadataArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetAttachmentsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _outlook_param_pb2.GetAttachmentsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_outlook_param_pb2.GetAttachmentsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorPutItemsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _outlook_param_pb2.PutItemsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_outlook_param_pb2.PutItemsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorCreateFolderPathArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _outlook_param_pb2.CreateFolderPathArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_outlook_param_pb2.CreateFolderPathArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorPoxAutodiscoverArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _outlook_param_pb2.PoxAutodiscoverArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_outlook_param_pb2.PoxAutodiscoverArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetUserSettingsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _outlook_param_pb2.GetUserSettingsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_outlook_param_pb2.GetUserSettingsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorFindFolderArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _outlook_param_pb2.FindFolderArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_outlook_param_pb2.FindFolderArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetFolderArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _outlook_param_pb2.GetFolderArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_outlook_param_pb2.GetFolderArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorCreateFolderOutlookArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _outlook_param_pb2.CreateFolderOutlookArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_outlook_param_pb2.CreateFolderOutlookArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorCreateFolderOutlookPathArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _outlook_param_pb2.CreateFolderOutlookPathArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_outlook_param_pb2.CreateFolderOutlookPathArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorUpdateFolderArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _outlook_param_pb2.UpdateFolderArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_outlook_param_pb2.UpdateFolderArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorValidateGraphCredentialsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.ValidateGraphCredentialsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.ValidateGraphCredentialsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetUsersArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetUsersArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetUsersArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGenericGetRequestArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GenericGetRequestArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GenericGetRequestArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetGroupsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetGroupsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetGroupsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSitesArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetSitesArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetSitesArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetAllEntitiesArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetAllEntitiesArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetAllEntitiesArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetEntityDrivesArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetEntityDrivesArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetEntityDrivesArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetDriveDeltaArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetDriveDeltaArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetDriveDeltaArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetItemPermissionsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetItemPermissionsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetItemPermissionsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetItemArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetItemArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetItemArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetFileContentPartialArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetFileContentPartialArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetFileContentPartialArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetFileContentArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetFileContentArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetFileContentArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorBatchRequestArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.BatchRequestArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.BatchRequestArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGenericBatchRequestArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GenericBatchRequestArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GenericBatchRequestArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorCreateFolderArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.CreateFolderArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.CreateFolderArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorCreateGroupArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.CreateGroupArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.CreateGroupArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorCreateUploadSessionArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.CreateUploadSessionArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.CreateUploadSessionArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorPutFileContentPartialArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.PutFileContentPartialArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.PutFileContentPartialArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorPutFileContentArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.PutFileContentArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.PutFileContentArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetListsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetListsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetListsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSiteDrivesArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetSiteDrivesArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetSiteDrivesArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetListItemsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetListItemsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetListItemsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetMailboxUsageDetailsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetMailboxUsageDetailsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetMailboxUsageDetailsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSiteInfoArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetSiteInfoArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetSiteInfoArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSubSitesArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetSubSitesArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetSubSitesArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorRestorePermissionsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.RestorePermissionsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.RestorePermissionsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetGroupOwnersArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetGroupOwnersArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetGroupOwnersArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetGroupMembersArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetGroupMembersArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetGroupMembersArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSubscribedSkusArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetSubscribedSkusArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetSubscribedSkusArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetGroupDeltaArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetGroupDeltaArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetGroupDeltaArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorAddUsersToGroupArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.AddUsersToGroupArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.AddUsersToGroupArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorCreateTeamChannelsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.CreateTeamChannelsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.CreateTeamChannelsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetGroupSiteArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetGroupSiteArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetGroupSiteArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetTeamsChannelsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetTeamsChannelsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetTeamsChannelsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetTeamsChannelDriveArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetTeamsChannelDriveArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetTeamsChannelDriveArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetTeamArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetTeamArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetTeamArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetChannelSiteArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetChannelSiteArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetChannelSiteArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorUpdateTeamChannelArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.UpdateTeamChannelArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.UpdateTeamChannelArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorCreateTeamArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.CreateTeamArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.CreateTeamArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetChannelInfoArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetChannelInfoArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetChannelInfoArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorUpdateGroupArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.UpdateGroupArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.UpdateGroupArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorUpdateTeamArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.UpdateTeamArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.UpdateTeamArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorCreateSiteListArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.CreateSiteListArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.CreateSiteListArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetGroupUsageDetailsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetGroupUsageDetailsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetGroupUsageDetailsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetAzureApplicationsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetAzureApplicationsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetAzureApplicationsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorCreateAzureApplicationsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.CreateAzureApplicationsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.CreateAzureApplicationsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorDeletePermissionArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.DeletePermissionArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.DeletePermissionArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorUpdateFileContentArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.UpdateFileContentArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.UpdateFileContentArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorCreateSystemFolderArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.CreateSystemFolderArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.CreateSystemFolderArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorCreateSiteAssetsListArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.CreateSiteAssetsListArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.CreateSiteAssetsListArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetWebIdsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.GetWebIdsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.GetWebIdsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSiteInformationArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.GetSiteInformationArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.GetSiteInformationArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorUpdateFileContentPartialArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.UpdateFileContentPartialArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.UpdateFileContentPartialArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSPListsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.GetSPListsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.GetSPListsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSiteScriptFromListArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.GetSiteScriptFromListArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.GetSiteScriptFromListArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorExecuteTemplateScriptArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.ExecuteTemplateScriptArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.ExecuteTemplateScriptArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSPListItemsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.GetSPListItemsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.GetSPListItemsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorPutSPListItemsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.PutSPListItemsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.PutSPListItemsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSPListChangesArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.GetSPListChangesArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.GetSPListChangesArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSharepointHostNameArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetSharepointHostNameArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetSharepointHostNameArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorDeleteM365GroupArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.DeleteM365GroupArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.DeleteM365GroupArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetValidGroupOwnerArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetValidGroupOwnerArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetValidGroupOwnerArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetListMessagesArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetListMessagesArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetListMessagesArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetMessageArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetMessageArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetMessageArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSiteAdminsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.GetSiteAdminsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.GetSiteAdminsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorSetSiteAdminsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.SetSiteAdminsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.SetSiteAdminsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSiteUsersArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.GetSiteUsersArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.GetSiteUsersArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetChatMessagesArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetChatMessagesArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetChatMessagesArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSPListItemCommentsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.GetSPListItemCommentsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.GetSPListItemCommentsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorPutSPListItemCommentsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.PutSPListItemCommentsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.PutSPListItemCommentsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSPListItemPermissionsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.GetSPListItemPermissionsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.GetSPListItemPermissionsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorPutSPListItemPermissionsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.PutSPListItemPermissionsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.PutSPListItemPermissionsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSPFileByServerRelativeUrlArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.GetSPFileByServerRelativeUrlArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.GetSPFileByServerRelativeUrlArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSPObjectByServerRelativePathArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.GetSPObjectByServerRelativePathArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.GetSPObjectByServerRelativePathArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSPListItemAttachmentsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.GetSPListItemAttachmentsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.GetSPListItemAttachmentsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSPListItemAttachmentsContentArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.GetSPListItemAttachmentsContentArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.GetSPListItemAttachmentsContentArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorPutSPListItemAttachmentsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.PutSPListItemAttachmentsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.PutSPListItemAttachmentsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetSPListFieldsArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _sharepoint_params_pb2.GetSPListFieldsArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_sharepoint_params_pb2.GetSPListFieldsArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...

class O365EmulatorGetChatInfoArg(_message.Message):
    __slots__ = ("arg", "connector_params")
    ARG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_PARAMS_FIELD_NUMBER: _ClassVar[int]
    arg: _graph_params_pb2.GetChatInfoArg
    connector_params: _magneto_pb2.ConnectorParams
    def __init__(self, arg: _Optional[_Union[_graph_params_pb2.GetChatInfoArg, _Mapping]] = ..., connector_params: _Optional[_Union[_magneto_pb2.ConnectorParams, _Mapping]] = ...) -> None: ...
