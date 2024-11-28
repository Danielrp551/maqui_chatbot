from components.twilio_component import TwilioManager
from api_keys.api_keys import premora

twilio_manager = TwilioManager()
template_content_sid = premora
parameters = '{"1": "Enrique"}'  # JSON string con parámetros

sid = twilio_manager.send_template_message(
    to_number='+51945827800',
    template_content_sid=template_content_sid,
    parameters=parameters
)