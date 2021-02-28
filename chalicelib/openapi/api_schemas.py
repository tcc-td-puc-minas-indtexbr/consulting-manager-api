from marshmallow import Schema, fields

from chalicelib.http_resources.request_control import Pagination
from chalicelib.openapi.schemas import DeletionSchema, RequestControlSchema, MetaSchema, LinkSchema


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
