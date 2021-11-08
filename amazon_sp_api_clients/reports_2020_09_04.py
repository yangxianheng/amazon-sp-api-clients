from .base import BaseClient as __BaseClient, convert_bool
from typing import List as _List


class Error:
    """
    Error response returned when the request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "code" in data:
            self.code: str = str(data["code"])
        else:
            self.code: str = None
        if "message" in data:
            self.message: str = str(data["message"])
        else:
            self.message: str = None
        if "details" in data:
            self.details: str = str(data["details"])
        else:
            self.details: str = None


class ReportDocumentEncryptionDetails:
    """
    Encryption details required for decryption of a report document's contents.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "standard" in data:
            self.standard: str = str(data["standard"])
        else:
            self.standard: str = None
        if "initializationVector" in data:
            self.initializationVector: str = str(data["initializationVector"])
        else:
            self.initializationVector: str = None
        if "key" in data:
            self.key: str = str(data["key"])
        else:
            self.key: str = None


class Report:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "marketplaceIds" in data:
            self.marketplaceIds: _List[str] = [str(datum) for datum in data["marketplaceIds"]]
        else:
            self.marketplaceIds: _List[str] = []
        if "reportId" in data:
            self.reportId: str = str(data["reportId"])
        else:
            self.reportId: str = None
        if "reportType" in data:
            self.reportType: str = str(data["reportType"])
        else:
            self.reportType: str = None
        if "dataStartTime" in data:
            self.dataStartTime: str = str(data["dataStartTime"])
        else:
            self.dataStartTime: str = None
        if "dataEndTime" in data:
            self.dataEndTime: str = str(data["dataEndTime"])
        else:
            self.dataEndTime: str = None
        if "reportScheduleId" in data:
            self.reportScheduleId: str = str(data["reportScheduleId"])
        else:
            self.reportScheduleId: str = None
        if "createdTime" in data:
            self.createdTime: str = str(data["createdTime"])
        else:
            self.createdTime: str = None
        if "processingStatus" in data:
            self.processingStatus: str = str(data["processingStatus"])
        else:
            self.processingStatus: str = None
        if "processingStartTime" in data:
            self.processingStartTime: str = str(data["processingStartTime"])
        else:
            self.processingStartTime: str = None
        if "processingEndTime" in data:
            self.processingEndTime: str = str(data["processingEndTime"])
        else:
            self.processingEndTime: str = None
        if "reportDocumentId" in data:
            self.reportDocumentId: str = str(data["reportDocumentId"])
        else:
            self.reportDocumentId: str = None


class CreateReportScheduleSpecification:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "reportType" in data:
            self.reportType: str = str(data["reportType"])
        else:
            self.reportType: str = None
        if "marketplaceIds" in data:
            self.marketplaceIds: _List[str] = [str(datum) for datum in data["marketplaceIds"]]
        else:
            self.marketplaceIds: _List[str] = []
        if "reportOptions" in data:
            self.reportOptions: ReportOptions = ReportOptions(data["reportOptions"])
        else:
            self.reportOptions: ReportOptions = None
        if "period" in data:
            self.period: str = str(data["period"])
        else:
            self.period: str = None
        if "nextReportCreationTime" in data:
            self.nextReportCreationTime: str = str(data["nextReportCreationTime"])
        else:
            self.nextReportCreationTime: str = None


class CreateReportSpecification:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "reportOptions" in data:
            self.reportOptions: ReportOptions = ReportOptions(data["reportOptions"])
        else:
            self.reportOptions: ReportOptions = None
        if "reportType" in data:
            self.reportType: str = str(data["reportType"])
        else:
            self.reportType: str = None
        if "dataStartTime" in data:
            self.dataStartTime: str = str(data["dataStartTime"])
        else:
            self.dataStartTime: str = None
        if "dataEndTime" in data:
            self.dataEndTime: str = str(data["dataEndTime"])
        else:
            self.dataEndTime: str = None
        if "marketplaceIds" in data:
            self.marketplaceIds: _List[str] = [str(datum) for datum in data["marketplaceIds"]]
        else:
            self.marketplaceIds: _List[str] = []


class ReportOptions:
    """
    Additional information passed to reports. This varies by report type.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data


class ReportSchedule:
    """
    Detailed information about a report schedule.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "reportScheduleId" in data:
            self.reportScheduleId: str = str(data["reportScheduleId"])
        else:
            self.reportScheduleId: str = None
        if "reportType" in data:
            self.reportType: str = str(data["reportType"])
        else:
            self.reportType: str = None
        if "marketplaceIds" in data:
            self.marketplaceIds: _List[str] = [str(datum) for datum in data["marketplaceIds"]]
        else:
            self.marketplaceIds: _List[str] = []
        if "reportOptions" in data:
            self.reportOptions: ReportOptions = ReportOptions(data["reportOptions"])
        else:
            self.reportOptions: ReportOptions = None
        if "period" in data:
            self.period: str = str(data["period"])
        else:
            self.period: str = None
        if "nextReportCreationTime" in data:
            self.nextReportCreationTime: str = str(data["nextReportCreationTime"])
        else:
            self.nextReportCreationTime: str = None


class CreateReportResult:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "reportId" in data:
            self.reportId: str = str(data["reportId"])
        else:
            self.reportId: str = None


class GetReportsResponse:
    """
    The response for the getReports operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: ReportList = ReportList(data["payload"])
        else:
            self.payload: ReportList = None
        if "nextToken" in data:
            self.nextToken: str = str(data["nextToken"])
        else:
            self.nextToken: str = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateReportResponse:
    """
    The response for the createReport operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: CreateReportResult = CreateReportResult(data["payload"])
        else:
            self.payload: CreateReportResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CancelReportResponse:
    """
    The response for the cancelReport operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CancelReportScheduleResponse:
    """
    The response for the cancelReportSchedule operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetReportResponse:
    """
    The response for the getReport operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: Report = Report(data["payload"])
        else:
            self.payload: Report = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetReportSchedulesResponse:
    """
    The response for the getReportSchedules operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: ReportScheduleList = ReportScheduleList(data["payload"])
        else:
            self.payload: ReportScheduleList = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class GetReportScheduleResponse:
    """
    The response for the getReportSchedule operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: ReportSchedule = ReportSchedule(data["payload"])
        else:
            self.payload: ReportSchedule = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class CreateReportScheduleResult:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "reportScheduleId" in data:
            self.reportScheduleId: str = str(data["reportScheduleId"])
        else:
            self.reportScheduleId: str = None


class CreateReportScheduleResponse:
    """
    The response for the createReportSchedule operation.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: CreateReportScheduleResult = CreateReportScheduleResult(data["payload"])
        else:
            self.payload: CreateReportScheduleResult = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class ReportDocument:
    """ """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "reportDocumentId" in data:
            self.reportDocumentId: str = str(data["reportDocumentId"])
        else:
            self.reportDocumentId: str = None
        if "url" in data:
            self.url: str = str(data["url"])
        else:
            self.url: str = None
        if "encryptionDetails" in data:
            self.encryptionDetails: ReportDocumentEncryptionDetails = ReportDocumentEncryptionDetails(
                data["encryptionDetails"]
            )
        else:
            self.encryptionDetails: ReportDocumentEncryptionDetails = None
        if "compressionAlgorithm" in data:
            self.compressionAlgorithm: str = str(data["compressionAlgorithm"])
        else:
            self.compressionAlgorithm: str = None


class GetReportDocumentResponse:
    """
    Response schema.
    """

    def __init__(self, data):
        super().__init__()
        self.data = data
        if "payload" in data:
            self.payload: ReportDocument = ReportDocument(data["payload"])
        else:
            self.payload: ReportDocument = None
        if "errors" in data:
            self.errors: ErrorList = ErrorList(data["errors"])
        else:
            self.errors: ErrorList = None


class ErrorList(list, _List["Error"]):
    """
    A list of error responses returned when a request is unsuccessful.
    """

    def __init__(self, data):
        super().__init__([Error(datum) for datum in data])
        self.data = data


class ReportList(list, _List["Report"]):
    """ """

    def __init__(self, data):
        super().__init__([Report(datum) for datum in data])
        self.data = data


class ReportScheduleList(list, _List["ReportSchedule"]):
    """ """

    def __init__(self, data):
        super().__init__([ReportSchedule(datum) for datum in data])
        self.data = data


class Reports20200904Client(__BaseClient):
    def getReports(
        self,
        reportTypes: _List[str] = None,
        processingStatuses: _List[str] = None,
        marketplaceIds: _List[str] = None,
        pageSize: int = None,
        createdSince: str = None,
        createdUntil: str = None,
        nextToken: str = None,
    ):
        """
                Returns report details for the reports that match the filters that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/reports/2020-09-04/reports"
        params = {}
        if reportTypes is not None:
            params["reportTypes"] = ",".join(map(str, reportTypes))
        if processingStatuses is not None:
            params["processingStatuses"] = ",".join(map(str, processingStatuses))
        if marketplaceIds is not None:
            params["marketplaceIds"] = ",".join(map(str, marketplaceIds))
        if pageSize is not None:
            params["pageSize"] = pageSize
        if createdSince is not None:
            params["createdSince"] = createdSince
        if createdUntil is not None:
            params["createdUntil"] = createdUntil
        if nextToken is not None:
            params["nextToken"] = nextToken
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        return {
            200: GetReportsResponse,
            400: GetReportsResponse,
            401: GetReportsResponse,
            403: GetReportsResponse,
            404: GetReportsResponse,
            415: GetReportsResponse,
            429: GetReportsResponse,
            500: GetReportsResponse,
            503: GetReportsResponse,
        }[response.status_code](self._get_response_json(response))

    def createReport(
        self,
        data: CreateReportSpecification,
    ):
        """
                Creates a report.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/reports/2020-09-04/reports"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        return {
            202: CreateReportResponse,
            400: CreateReportResponse,
            401: CreateReportResponse,
            403: CreateReportResponse,
            404: CreateReportResponse,
            415: CreateReportResponse,
            429: CreateReportResponse,
            500: CreateReportResponse,
            503: CreateReportResponse,
        }[response.status_code](self._get_response_json(response))

    def getReport(
        self,
        reportId: str,
    ):
        """
                Returns report details (including the reportDocumentId, if available) for the report that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 2.0 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/reports/2020-09-04/reports/{reportId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        return {
            200: GetReportResponse,
            400: GetReportResponse,
            401: GetReportResponse,
            403: GetReportResponse,
            404: GetReportResponse,
            415: GetReportResponse,
            429: GetReportResponse,
            500: GetReportResponse,
            503: GetReportResponse,
        }[response.status_code](self._get_response_json(response))

    def cancelReport(
        self,
        reportId: str,
    ):
        """
                Cancels the report that you specify. Only reports with processingStatus=IN_QUEUE can be cancelled. Cancelled reports are returned in subsequent calls to the getReport and getReports operations.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/reports/2020-09-04/reports/{reportId}"
        params = {}
        response = self.request(
            path=url,
            method="DELETE",
            params=params,
        )
        return {
            200: CancelReportResponse,
            400: CancelReportResponse,
            401: CancelReportResponse,
            403: CancelReportResponse,
            404: CancelReportResponse,
            415: CancelReportResponse,
            429: CancelReportResponse,
            500: CancelReportResponse,
            503: CancelReportResponse,
        }[response.status_code](self._get_response_json(response))

    def getReportSchedules(
        self,
        reportTypes: _List[str],
    ):
        """
                Returns report schedule details that match the filters that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/reports/2020-09-04/schedules"
        params = {}
        if reportTypes is not None:
            params["reportTypes"] = ",".join(map(str, reportTypes))
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        return {
            200: GetReportSchedulesResponse,
            400: GetReportSchedulesResponse,
            401: GetReportSchedulesResponse,
            403: GetReportSchedulesResponse,
            404: GetReportSchedulesResponse,
            415: GetReportSchedulesResponse,
            429: GetReportSchedulesResponse,
            500: GetReportSchedulesResponse,
            503: GetReportSchedulesResponse,
        }[response.status_code](self._get_response_json(response))

    def createReportSchedule(
        self,
        data: CreateReportScheduleSpecification,
    ):
        """
                Creates a report schedule. If a report schedule with the same report type and marketplace IDs already exists, it will be cancelled and replaced with this one.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/reports/2020-09-04/schedules"
        params = {}
        response = self.request(
            path=url,
            method="POST",
            params=params,
            data=data.data,
        )
        return {
            201: CreateReportScheduleResponse,
            400: CreateReportScheduleResponse,
            401: CreateReportScheduleResponse,
            403: CreateReportScheduleResponse,
            404: CreateReportScheduleResponse,
            415: CreateReportScheduleResponse,
            429: CreateReportScheduleResponse,
            500: CreateReportScheduleResponse,
            503: CreateReportScheduleResponse,
        }[response.status_code](self._get_response_json(response))

    def getReportSchedule(
        self,
        reportScheduleId: str,
    ):
        """
                Returns report schedule details for the report schedule that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/reports/2020-09-04/schedules/{reportScheduleId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        return {
            200: GetReportScheduleResponse,
            400: GetReportScheduleResponse,
            401: GetReportScheduleResponse,
            403: GetReportScheduleResponse,
            404: GetReportScheduleResponse,
            415: GetReportScheduleResponse,
            429: GetReportScheduleResponse,
            500: GetReportScheduleResponse,
            503: GetReportScheduleResponse,
        }[response.status_code](self._get_response_json(response))

    def cancelReportSchedule(
        self,
        reportScheduleId: str,
    ):
        """
                Cancels the report schedule that you specify.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0222 | 10 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/reports/2020-09-04/schedules/{reportScheduleId}"
        params = {}
        response = self.request(
            path=url,
            method="DELETE",
            params=params,
        )
        return {
            200: CancelReportScheduleResponse,
            400: CancelReportScheduleResponse,
            401: CancelReportScheduleResponse,
            403: CancelReportScheduleResponse,
            404: CancelReportScheduleResponse,
            415: CancelReportScheduleResponse,
            429: CancelReportScheduleResponse,
            500: CancelReportScheduleResponse,
            503: CancelReportScheduleResponse,
        }[response.status_code](self._get_response_json(response))

    def getReportDocument(
        self,
        reportDocumentId: str,
    ):
        """
                Returns the information required for retrieving a report document's contents. This includes a presigned URL for the report document as well as the information required to decrypt the document's contents.
        **Usage Plan:**
        | Rate (requests per second) | Burst |
        | ---- | ---- |
        | 0.0167 | 15 |
        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.
        """
        url = f"/reports/2020-09-04/documents/{reportDocumentId}"
        params = {}
        response = self.request(
            path=url,
            method="GET",
            params=params,
        )
        return {
            200: GetReportDocumentResponse,
            400: GetReportDocumentResponse,
            401: GetReportDocumentResponse,
            403: GetReportDocumentResponse,
            404: GetReportDocumentResponse,
            415: GetReportDocumentResponse,
            429: GetReportDocumentResponse,
            500: GetReportDocumentResponse,
            503: GetReportDocumentResponse,
        }[response.status_code](self._get_response_json(response))
