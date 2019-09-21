from tornado.web import url
from handlers import *

handlers = [
	url(r"/api/data/([^/]+)?", DataHandler),
	# url(r"/files/upload/update", StreamHandler),
	# url(r"/files/upload/license", UploadLicenseHandler),
	# url(r"/files/upload/restore", RestoreBackupHandler),
	# url(r"/files/download/cert", DownloadSslCertificateHandler),
	# url(r"/files/download/support-zip", ChassisSupportHandler),
	# url(r"/files/download/backup-zip", BackUpDBHandler ),
	# # endpoint only for nuxt image
	# url(r"/internal/apps", GetAppsHandler),
]