from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class YodaConfigProto(_message.Message):
    __slots__ = ("gandalf_master_lock_name", "lookup_master_url", "get_report_url", "get_pending_info_url", "master_status_url", "get_cracked_file_versions_url", "extract_file_range_url", "work_items_details_url", "delete_work_items_url", "save_map_reduce_entity_url", "delete_map_reduce_entity_url", "get_map_reduce_entity_url", "run_mr_instance_url", "get_mr_instance_url", "kill_mr_instance_url", "analyse_jar_url", "get_mr_jar_upload_path_url", "extract_nfs_file_range_url", "gc_snapshots_url", "vm_read_dir_url", "vm_file_stat_url", "cracked_files_restore_info_url", "vm_volume_info_url", "consume_audit_logs_url", "gc_audit_logs_url", "gc_archival_dbs_url", "gc_zip_checkpoints_url", "gc_librarian_migration_url", "fix_es_indices_url", "read_dir_url", "file_stat_url", "object_indexing_details_url", "corrupt_vms_details_url", "mr_result_formats_url", "get_mr_aux_data_url", "save_mr_aux_data_url", "delete_mr_aux_data_url", "start_librarian_migration_url", "librarian_migration_work_items_details_url", "librarian_migration_finished_status_url", "delete_librarian_migration_work_items_url", "clear_finished_librarian_migration_for_cfileindex_url", "consume_pubsub_data_url", "apply_tags_url", "remove_tags_url", "create_tag_url", "update_tag_url", "get_or_list_tags_url", "delete_tag_url", "task_details_url", "gc_tags_url", "add_tenant_cloud_config_url", "get_tenant_cloud_config_url", "toggle_slave_dispatcher_url", "es_migration_work_items_details_url", "delete_es_migration_work_items_url", "es_migration_status_url", "update_es_migration_status_url", "start_es_migration_url", "finish_es_migration_url", "abort_es_migration_url", "slow_directories_url", "remove_slow_directories_url", "recreate_clone_views_url", "slow_objects_url", "work_items_status_url")
    GANDALF_MASTER_LOCK_NAME_FIELD_NUMBER: _ClassVar[int]
    LOOKUP_MASTER_URL_FIELD_NUMBER: _ClassVar[int]
    GET_REPORT_URL_FIELD_NUMBER: _ClassVar[int]
    GET_PENDING_INFO_URL_FIELD_NUMBER: _ClassVar[int]
    MASTER_STATUS_URL_FIELD_NUMBER: _ClassVar[int]
    GET_CRACKED_FILE_VERSIONS_URL_FIELD_NUMBER: _ClassVar[int]
    EXTRACT_FILE_RANGE_URL_FIELD_NUMBER: _ClassVar[int]
    WORK_ITEMS_DETAILS_URL_FIELD_NUMBER: _ClassVar[int]
    DELETE_WORK_ITEMS_URL_FIELD_NUMBER: _ClassVar[int]
    SAVE_MAP_REDUCE_ENTITY_URL_FIELD_NUMBER: _ClassVar[int]
    DELETE_MAP_REDUCE_ENTITY_URL_FIELD_NUMBER: _ClassVar[int]
    GET_MAP_REDUCE_ENTITY_URL_FIELD_NUMBER: _ClassVar[int]
    RUN_MR_INSTANCE_URL_FIELD_NUMBER: _ClassVar[int]
    GET_MR_INSTANCE_URL_FIELD_NUMBER: _ClassVar[int]
    KILL_MR_INSTANCE_URL_FIELD_NUMBER: _ClassVar[int]
    ANALYSE_JAR_URL_FIELD_NUMBER: _ClassVar[int]
    GET_MR_JAR_UPLOAD_PATH_URL_FIELD_NUMBER: _ClassVar[int]
    EXTRACT_NFS_FILE_RANGE_URL_FIELD_NUMBER: _ClassVar[int]
    GC_SNAPSHOTS_URL_FIELD_NUMBER: _ClassVar[int]
    VM_READ_DIR_URL_FIELD_NUMBER: _ClassVar[int]
    VM_FILE_STAT_URL_FIELD_NUMBER: _ClassVar[int]
    CRACKED_FILES_RESTORE_INFO_URL_FIELD_NUMBER: _ClassVar[int]
    VM_VOLUME_INFO_URL_FIELD_NUMBER: _ClassVar[int]
    CONSUME_AUDIT_LOGS_URL_FIELD_NUMBER: _ClassVar[int]
    GC_AUDIT_LOGS_URL_FIELD_NUMBER: _ClassVar[int]
    GC_ARCHIVAL_DBS_URL_FIELD_NUMBER: _ClassVar[int]
    GC_ZIP_CHECKPOINTS_URL_FIELD_NUMBER: _ClassVar[int]
    GC_LIBRARIAN_MIGRATION_URL_FIELD_NUMBER: _ClassVar[int]
    FIX_ES_INDICES_URL_FIELD_NUMBER: _ClassVar[int]
    READ_DIR_URL_FIELD_NUMBER: _ClassVar[int]
    FILE_STAT_URL_FIELD_NUMBER: _ClassVar[int]
    OBJECT_INDEXING_DETAILS_URL_FIELD_NUMBER: _ClassVar[int]
    CORRUPT_VMS_DETAILS_URL_FIELD_NUMBER: _ClassVar[int]
    MR_RESULT_FORMATS_URL_FIELD_NUMBER: _ClassVar[int]
    GET_MR_AUX_DATA_URL_FIELD_NUMBER: _ClassVar[int]
    SAVE_MR_AUX_DATA_URL_FIELD_NUMBER: _ClassVar[int]
    DELETE_MR_AUX_DATA_URL_FIELD_NUMBER: _ClassVar[int]
    START_LIBRARIAN_MIGRATION_URL_FIELD_NUMBER: _ClassVar[int]
    LIBRARIAN_MIGRATION_WORK_ITEMS_DETAILS_URL_FIELD_NUMBER: _ClassVar[int]
    LIBRARIAN_MIGRATION_FINISHED_STATUS_URL_FIELD_NUMBER: _ClassVar[int]
    DELETE_LIBRARIAN_MIGRATION_WORK_ITEMS_URL_FIELD_NUMBER: _ClassVar[int]
    CLEAR_FINISHED_LIBRARIAN_MIGRATION_FOR_CFILEINDEX_URL_FIELD_NUMBER: _ClassVar[int]
    CONSUME_PUBSUB_DATA_URL_FIELD_NUMBER: _ClassVar[int]
    APPLY_TAGS_URL_FIELD_NUMBER: _ClassVar[int]
    REMOVE_TAGS_URL_FIELD_NUMBER: _ClassVar[int]
    CREATE_TAG_URL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TAG_URL_FIELD_NUMBER: _ClassVar[int]
    GET_OR_LIST_TAGS_URL_FIELD_NUMBER: _ClassVar[int]
    DELETE_TAG_URL_FIELD_NUMBER: _ClassVar[int]
    TASK_DETAILS_URL_FIELD_NUMBER: _ClassVar[int]
    GC_TAGS_URL_FIELD_NUMBER: _ClassVar[int]
    ADD_TENANT_CLOUD_CONFIG_URL_FIELD_NUMBER: _ClassVar[int]
    GET_TENANT_CLOUD_CONFIG_URL_FIELD_NUMBER: _ClassVar[int]
    TOGGLE_SLAVE_DISPATCHER_URL_FIELD_NUMBER: _ClassVar[int]
    ES_MIGRATION_WORK_ITEMS_DETAILS_URL_FIELD_NUMBER: _ClassVar[int]
    DELETE_ES_MIGRATION_WORK_ITEMS_URL_FIELD_NUMBER: _ClassVar[int]
    ES_MIGRATION_STATUS_URL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ES_MIGRATION_STATUS_URL_FIELD_NUMBER: _ClassVar[int]
    START_ES_MIGRATION_URL_FIELD_NUMBER: _ClassVar[int]
    FINISH_ES_MIGRATION_URL_FIELD_NUMBER: _ClassVar[int]
    ABORT_ES_MIGRATION_URL_FIELD_NUMBER: _ClassVar[int]
    SLOW_DIRECTORIES_URL_FIELD_NUMBER: _ClassVar[int]
    REMOVE_SLOW_DIRECTORIES_URL_FIELD_NUMBER: _ClassVar[int]
    RECREATE_CLONE_VIEWS_URL_FIELD_NUMBER: _ClassVar[int]
    SLOW_OBJECTS_URL_FIELD_NUMBER: _ClassVar[int]
    WORK_ITEMS_STATUS_URL_FIELD_NUMBER: _ClassVar[int]
    gandalf_master_lock_name: str
    lookup_master_url: str
    get_report_url: str
    get_pending_info_url: str
    master_status_url: str
    get_cracked_file_versions_url: str
    extract_file_range_url: str
    work_items_details_url: str
    delete_work_items_url: str
    save_map_reduce_entity_url: str
    delete_map_reduce_entity_url: str
    get_map_reduce_entity_url: str
    run_mr_instance_url: str
    get_mr_instance_url: str
    kill_mr_instance_url: str
    analyse_jar_url: str
    get_mr_jar_upload_path_url: str
    extract_nfs_file_range_url: str
    gc_snapshots_url: str
    vm_read_dir_url: str
    vm_file_stat_url: str
    cracked_files_restore_info_url: str
    vm_volume_info_url: str
    consume_audit_logs_url: str
    gc_audit_logs_url: str
    gc_archival_dbs_url: str
    gc_zip_checkpoints_url: str
    gc_librarian_migration_url: str
    fix_es_indices_url: str
    read_dir_url: str
    file_stat_url: str
    object_indexing_details_url: str
    corrupt_vms_details_url: str
    mr_result_formats_url: str
    get_mr_aux_data_url: str
    save_mr_aux_data_url: str
    delete_mr_aux_data_url: str
    start_librarian_migration_url: str
    librarian_migration_work_items_details_url: str
    librarian_migration_finished_status_url: str
    delete_librarian_migration_work_items_url: str
    clear_finished_librarian_migration_for_cfileindex_url: str
    consume_pubsub_data_url: str
    apply_tags_url: str
    remove_tags_url: str
    create_tag_url: str
    update_tag_url: str
    get_or_list_tags_url: str
    delete_tag_url: str
    task_details_url: str
    gc_tags_url: str
    add_tenant_cloud_config_url: str
    get_tenant_cloud_config_url: str
    toggle_slave_dispatcher_url: str
    es_migration_work_items_details_url: str
    delete_es_migration_work_items_url: str
    es_migration_status_url: str
    update_es_migration_status_url: str
    start_es_migration_url: str
    finish_es_migration_url: str
    abort_es_migration_url: str
    slow_directories_url: str
    remove_slow_directories_url: str
    recreate_clone_views_url: str
    slow_objects_url: str
    work_items_status_url: str
    def __init__(self, gandalf_master_lock_name: _Optional[str] = ..., lookup_master_url: _Optional[str] = ..., get_report_url: _Optional[str] = ..., get_pending_info_url: _Optional[str] = ..., master_status_url: _Optional[str] = ..., get_cracked_file_versions_url: _Optional[str] = ..., extract_file_range_url: _Optional[str] = ..., work_items_details_url: _Optional[str] = ..., delete_work_items_url: _Optional[str] = ..., save_map_reduce_entity_url: _Optional[str] = ..., delete_map_reduce_entity_url: _Optional[str] = ..., get_map_reduce_entity_url: _Optional[str] = ..., run_mr_instance_url: _Optional[str] = ..., get_mr_instance_url: _Optional[str] = ..., kill_mr_instance_url: _Optional[str] = ..., analyse_jar_url: _Optional[str] = ..., get_mr_jar_upload_path_url: _Optional[str] = ..., extract_nfs_file_range_url: _Optional[str] = ..., gc_snapshots_url: _Optional[str] = ..., vm_read_dir_url: _Optional[str] = ..., vm_file_stat_url: _Optional[str] = ..., cracked_files_restore_info_url: _Optional[str] = ..., vm_volume_info_url: _Optional[str] = ..., consume_audit_logs_url: _Optional[str] = ..., gc_audit_logs_url: _Optional[str] = ..., gc_archival_dbs_url: _Optional[str] = ..., gc_zip_checkpoints_url: _Optional[str] = ..., gc_librarian_migration_url: _Optional[str] = ..., fix_es_indices_url: _Optional[str] = ..., read_dir_url: _Optional[str] = ..., file_stat_url: _Optional[str] = ..., object_indexing_details_url: _Optional[str] = ..., corrupt_vms_details_url: _Optional[str] = ..., mr_result_formats_url: _Optional[str] = ..., get_mr_aux_data_url: _Optional[str] = ..., save_mr_aux_data_url: _Optional[str] = ..., delete_mr_aux_data_url: _Optional[str] = ..., start_librarian_migration_url: _Optional[str] = ..., librarian_migration_work_items_details_url: _Optional[str] = ..., librarian_migration_finished_status_url: _Optional[str] = ..., delete_librarian_migration_work_items_url: _Optional[str] = ..., clear_finished_librarian_migration_for_cfileindex_url: _Optional[str] = ..., consume_pubsub_data_url: _Optional[str] = ..., apply_tags_url: _Optional[str] = ..., remove_tags_url: _Optional[str] = ..., create_tag_url: _Optional[str] = ..., update_tag_url: _Optional[str] = ..., get_or_list_tags_url: _Optional[str] = ..., delete_tag_url: _Optional[str] = ..., task_details_url: _Optional[str] = ..., gc_tags_url: _Optional[str] = ..., add_tenant_cloud_config_url: _Optional[str] = ..., get_tenant_cloud_config_url: _Optional[str] = ..., toggle_slave_dispatcher_url: _Optional[str] = ..., es_migration_work_items_details_url: _Optional[str] = ..., delete_es_migration_work_items_url: _Optional[str] = ..., es_migration_status_url: _Optional[str] = ..., update_es_migration_status_url: _Optional[str] = ..., start_es_migration_url: _Optional[str] = ..., finish_es_migration_url: _Optional[str] = ..., abort_es_migration_url: _Optional[str] = ..., slow_directories_url: _Optional[str] = ..., remove_slow_directories_url: _Optional[str] = ..., recreate_clone_views_url: _Optional[str] = ..., slow_objects_url: _Optional[str] = ..., work_items_status_url: _Optional[str] = ...) -> None: ...
