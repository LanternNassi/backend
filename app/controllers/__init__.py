# import all controllers

from .index import IndexView
from .users import (
    UsersView, UserLoginView, UserEmailVerificationView,
    EmailVerificationRequest, ForgotPasswordView, ResetPasswordView,
    UserDetailView, AdminLoginView, OAuthView, UserDataSummaryView, UserAdminUpdateView, UserActivitesView)
from .deployments import DeploymentsView
from .clusters import (
    ClustersView, ClusterDetailView, ClusterNamespacesView,
    ClusterNamespaceDetailView, ClusterNodesView, ClusterNodeDetailView,
    ClusterDeploymentsView, ClusterDeploymentDetailView, ClusterPvcsView,
    ClusterPvcDetailView, ClusterPVsView, ClusterPVDetailView,
    ClusterPodsView, ClusterPodDetailView, ClusterServicesView,
    ClusterServiceDetailView, ClusterJobsView, ClusterJobDetailView,
    ClusterStorageClassView, ClusterStorageClassDetailView)
from .roles import RolesView, RolesDetailView
from .credit_assignments import CreditAssignmentView, CreditAssignmentDetailView
from .credits import CreditView, CreditDetailView
from .user_role import UserRolesView
from .transactions import TransactionRecordView, TransactionRecordDetailView, CreditTransactionRecordView, CreditPurchaseTransactionRecordView
from .project import (
    ProjectsView, ProjectDetailView, UserProjectsView, ProjectGetCostsView,
    ProjectCPUView, ProjectMemoryUsageView, ProjectNetworkRequestView, ProjectStorageUsageView)
from .app import (AppsView, ProjectAppsView, AppDetailView, AppLogsView,
                  AppCpuUsageView, AppMemoryUsageView, AppNetworkUsageView, AppStorageUsageView,
                  AppDataSummaryView, AppRevertView, AppReviseView)
from .registry import RegistriesView
from .project_database import (ProjectDatabaseView, ProjectDatabaseDetailView, ProjectDatabaseAdminView,
                               ProjectDatabaseAdminDetailView, ProjectDatabaseResetView, ProjectDatabaseAdminResetView,
                               ProjectDatabasePasswordResetView, ProjectDatabaseAdminPasswordResetView,
                               ProjectDatabaseRetrievePasswordView, ProjectDatabaseAdminRetrievePasswordView, DatabaseStatsView)
from .billing_invoice import (BillingInvoiceView,BillingInvoiceNotificationView)
from .system_status import SystemStatusView
from .project_users import ProjectUsersView, ProjectUsersTransferView, ProjectUsersHandleInviteView
