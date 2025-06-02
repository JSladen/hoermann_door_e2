import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import button
from esphome.const import ICON_FAN
from .. import uapbridge_ns, CONF_UAPBRIDGE_ID, UAPBridge

DEPENDENCIES = ["uapbridge"]

UAPBridgeButtonVent = uapbridge_ns.class_("UAPBridgeButtonVent", button.Button, cg.Component)
UAPBridgeButtonImpulse = uapbridge_ns.class_("UAPBridgeButtonImpulse", button.Button, cg.Component)
UAPBridgeButtonLight = uapbridge_ns.class_("UAPBridgeButtonLight", button.Button, cg.Component)

CONF_BUTTON_VENT = "vent_button"
CONF_BUTTON_IMPULSE = "impulse_button"
CONF_BUTTON_LIGHT = "light_button"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_UAPBRIDGE_ID): cv.use_id(UAPBridge),
        cv.Optional(CONF_BUTTON_VENT): button.button_schema(
            UAPBridgeButtonVent, icon=ICON_FAN
        ),
        cv.Optional(CONF_BUTTON_IMPULSE): button.button_schema(
            UAPBridgeButtonImpulse, icon="mdi:arrow-up-down"
        ),
        cv.Optional(CONF_BUTTON_LIGHT): button.button_schema(
            UAPBridgeButtonLight, icon="mdi:light"
        ),
    }
).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    parent = await cg.get_variable(config[CONF_UAPBRIDGE_ID])

    if conf := config.get(CONF_BUTTON_VENT):
        vent_button = await button.new_button(conf)
        await cg.register_component(vent_button, conf)
        cg.add(vent_button.set_uapbridge_parent(parent))

    if conf := config.get(CONF_BUTTON_IMPULSE):
        impulse_button = await button.new_button(conf)
        await cg.register_component(impulse_button, conf)
        cg.add(impulse_button.set_uapbridge_parent(parent))

    if conf := config.get(CONF_BUTTON_LIGHT):
        light_button = await button.new_button(conf)
        await cg.register_component(light_button, conf)
        cg.add(light_button.set_uapbridge_parent(parent))
