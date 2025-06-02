#include "uapbridge_button.h"
#include "esphome/core/log.h"

namespace esphome {
namespace uapbridge {

static const char* const TAG = "uapbridge.button";

void UAPBridgeButtonVent::press_action() {
  ESP_LOGD(TAG, "UAPBridgeButtonVent::press_action() - Triggering vent position");
  this->parent_->action_venting();
}

void UAPBridgeButtonImpulse::press_action() {
  ESP_LOGD(TAG, "UAPBridgeButtonImpulse::press_action() - Triggering impulse action");
  this->parent_->action_impulse();
}

void UAPBridgeButtonLight::press_action() {
  ESP_LOGD(TAG, "UAPBridgeButtonLight::press_action() - Triggering Light Toggle action");
  this->parent_->action_light();
}

}  // namespace uapbridge
}  // namespace esphome
