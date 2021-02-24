from marshmallow import Schema, fields

from chalicelib.http_resources.request_control import Pagination


class DeletionSchema(Schema):
    success = fields.Bool()
    code = fields.Int(required=True)
    label = fields.Str()
    message = fields.Str()
    params = fields.List(fields.Str())


class ErrorSchema(Schema):
    code = fields.Int(required=True)
    label = fields.Str()
    message = fields.Str()


class RequestControlSchema(Schema):
    offset = fields.Int(default=Pagination.OFFSET)
    limit = fields.Int(required=True, default=Pagination.LIMIT)
    total = fields.Int()
    count = fields.Int()


class MetaSchema(Schema):
    href = fields.URL()
    next = fields.URL()
    previous = fields.URL()
    first = fields.URL()
    last = fields.URL()


class LinkSchema(Schema):
    href = fields.Str()
    rel = fields.Str()
    method = fields.Str()


class PingSchema(Schema):
    message = fields.Str(example="PONG")


class AliveSchema(Schema):
    app = fields.Str(example="I'm alive!")


class ConsultingSchema(Schema):
    uuid = fields.UUID()
    businessArea = fields.Str(example="Jurídico")
    company = fields.Str(example="Razão Social")
    companyName = fields.Str(example="Nome Fantasia")
    cnpj = fields.Str()
    agreementDate = fields.Date()
    startDate = fields.Date()
    endDate = fields.Date()


class ConsultingCreateRequest(Schema):
    uuid = fields.UUID()
    businessArea = fields.Str()
    company = fields.Str()
    companyName = fields.Str()
    cnpj = fields.Str()
    agreementDate = fields.Date()
    startDate = fields.Date()
    endDate = fields.Date()


class ConsultingUpdateRequest(ConsultingCreateRequest):
    pass


class ConsultingListResponseSchema(Schema):
    data = fields.List(fields.Nested(ConsultingSchema))
    control = fields.Nested(RequestControlSchema)
    meta = fields.Nested(MetaSchema)
    links = fields.List(fields.Nested(LinkSchema))


class ConsultingGetResponseSchema(Schema):
    data = fields.Nested(ConsultingSchema)
    control = fields.Nested(RequestControlSchema)
    meta = fields.Nested(MetaSchema)
    links = fields.List(fields.Nested(LinkSchema))


class ConsultingCreateResponseSchema(ConsultingGetResponseSchema):
    pass


class ConsultingUpdateResponseSchema(ConsultingGetResponseSchema):
    pass


class ConsultingDeleteResponseSchema(ConsultingGetResponseSchema):
    data = fields.Nested(DeletionSchema)
