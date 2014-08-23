# -*- coding: utf-8 -*-
import logging
from jsonschema import validate
from jsonschema.exceptions import ValidationError

listener_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "usernames": {"type": "array", "items":  {"type": "string"}},
        "hashtags": {"type": "array", "items":  {"type": "string"}},
        "startDate": {"type": "string"},
        "endDate": {"type": "string"}
    },
    "required": ["usernames", "hashtags", "startDate", "endDate"]
}

logger = logging.getLogger('shema')


def check_json_listener(json):
    """
    Method to validate listener json
    """
    try:
        validate(json, listener_schema)
        return True
    except ValidationError, error:
        logger.error("Listener json invalid: %s", error)
        return False
