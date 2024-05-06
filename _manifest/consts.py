ENV_LINK_PREFIX = 'LINK_PREFIX'
ENV_SHIPPING_PATH_PREFIX = 'SHIPPING_PATH_PREFIX'
ENV_MANIFEST_PATH = 'MANIFEST_PATH'
ENV_TEST_MANIFEST_PATH = 'TEST_MANIFEST_PATH'

DEFAULT_LINK_PREFIX = 'https://raw.githubusercontent.com/logzio/documentation/master/'
DEFAULT_SHIPPING_PATH_PREFIX = 'docs/shipping/'
DEFAULT_MANIFEST_PATH = 'static/manifest.json'
DEFAULT_TEST_MANIFEST_PATH = '_manifest/test-manifest.json'

FIELD_COLLECTORS = 'collectors'
FIELD_AVAILABLE_FILTERS = 'tags'
FIELD_LINK = 'dataLink'
FIELD_ID = 'id'
FIELD_RECOMMENDED_FOR = 'recommendedFor'
FIELD_TITLE = 'title'
FIELD_DESCRIPTION = 'description'
FIELD_LOGO = 'logo'
FIELD_PRODUCT_TAGS = 'productTags'
FIELD_FILTER_TAGS = 'filterTags'
FIELD_OS_TAGS = 'osTags'
FIELD_DISPLAY_NAME = 'displayName'
FIELD_BUNDLES = 'bundle'
FIELD_BUNDLES_TYPE = 'type'
FIELD_BUNDLES_ID = 'id'

META_ID = 'id'
META_RECOMMENDED_FOR = 'recommendedfor'
META_TITLE = 'title'
META_OVERVIEW = 'overview'
META_LOGO = 'logo'
META_PRODUCT = 'product'
META_FILTERS = 'filters'
META_OS = 'os'
META_LOGS_DASHBOARDS = 'logs_dashboards'
META_LOGS_ALERTS = 'logs_alerts'
META_LOGS_TO_METRICS = 'logs2metrics'
META_METRICS_DASHBOARDS = 'metrics_dashboards'
META_METRICS_ALERTS = 'metrics_alerts'
META_DROP_FILTER = 'drop_filter'

BUNDLE_TYPE_OSD_DASHBOARD = 'OSD_DASHBOARD'
BUNDLE_TYPE_GRAFANA_DASHBOARD = 'GRAFANA_DASHBOARD'
BUNDLE_TYPE_LOGZ_ALERT = 'LOG_ALERT'
BUNDLE_TYPE_GRAFANA_ALERT = 'GRAFANA_ALERT'
BUNDLE_TYPE_LOGS_TO_METRICS = 'LOGS_TO_METRICS'
BUNDLE_DROP_FILTER = 'DROP_FILTER'

DOCS_PRODUCT_TYPE_LOGS = 'logs'
DOCS_PRODUCT_TYPE_METRICS = 'metrics'
DOCS_PRODUCT_TYPE_TRACES = 'tracing'
DOCS_PRODUCT_TYPE_SIEM = 'siem'

PRODUCT_TYPE_LOGS = 'LOG_ANALYTICS'
PRODUCT_TYPE_METRICS = 'METRICS'
PRODUCT_TYPE_TRACES = 'TRACING'
PRODUCT_TYPE_SIEM = 'SIEM'


MD_TO_MANIFEST_KEYS = {
    META_ID: FIELD_ID,
    META_RECOMMENDED_FOR: FIELD_RECOMMENDED_FOR,
    META_TITLE: FIELD_TITLE,
    META_OVERVIEW: FIELD_DESCRIPTION,
    META_LOGO: FIELD_LOGO,
    META_PRODUCT: FIELD_PRODUCT_TAGS,
    META_FILTERS: FIELD_FILTER_TAGS,
    META_OS: FIELD_OS_TAGS
}

META_TO_BUNDLE_TYPE = {
    META_LOGS_DASHBOARDS: BUNDLE_TYPE_OSD_DASHBOARD,
    META_LOGS_ALERTS: BUNDLE_TYPE_LOGZ_ALERT,
    META_METRICS_DASHBOARDS: BUNDLE_TYPE_GRAFANA_DASHBOARD,
    META_METRICS_ALERTS: BUNDLE_TYPE_GRAFANA_ALERT,
    META_LOGS_TO_METRICS: BUNDLE_TYPE_LOGS_TO_METRICS,
    META_DROP_FILTER: BUNDLE_DROP_FILTER
}

DOCS_TO_OBJ_PRODUCT_TYPE = {
    DOCS_PRODUCT_TYPE_LOGS: PRODUCT_TYPE_LOGS,
    DOCS_PRODUCT_TYPE_METRICS: PRODUCT_TYPE_METRICS,
    DOCS_PRODUCT_TYPE_TRACES: PRODUCT_TYPE_TRACES,
    DOCS_PRODUCT_TYPE_SIEM: PRODUCT_TYPE_SIEM
}

ARRAY_KEYS = [FIELD_PRODUCT_TAGS, FIELD_FILTER_TAGS, FIELD_OS_TAGS]
BUNDLE_META = [META_LOGS_DASHBOARDS, META_LOGS_ALERTS, META_LOGS_TO_METRICS, META_METRICS_DASHBOARDS,
               META_METRICS_ALERTS, META_DROP_FILTER]
