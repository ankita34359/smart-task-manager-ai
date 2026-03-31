from marshmallow import Schema, fields, validate, validates, validates_schema, ValidationError
from datetime import datetime, timezone

class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1, error="Title cannot be empty."))
    description = fields.Str(allow_none=True)
    status = fields.Str(validate=validate.OneOf(["TODO", "IN_PROGRESS", "DONE"]))
    priority = fields.Str(validate=validate.OneOf(["LOW", "MEDIUM", "HIGH"]))
    due_date = fields.DateTime(allow_none=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    @validates('due_date')
    def validate_due_date(self, value):
        if value:
            # Check if it's in the past
            now = datetime.now(timezone.utc)
            # Make value timezone aware if it's not
            if value.tzinfo is None:
                value = value.replace(tzinfo=timezone.utc)
            if value < now:
                raise ValidationError("due_date cannot be in the past.")

    @validates('title')
    def validate_title_content(self, value):
        if not value or not value.strip():
            raise ValidationError("Title cannot be logically empty.")

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
