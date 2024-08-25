# dns_app/utils.py
import json
from .models import Device, IDSLog
from django.utils import timezone


def parse_ids_logs(log_file):
    with open(log_file, "r") as f:
        logs = json.load(f)

    for log in logs:
        source_ip = log.get("src_ip")
        destination_ip = log.get("dest_ip")
        source_mac = log.get("src_mac")
        destination_mac = log.get("dest_mac")

        device = Device.objects.filter(ip_address=source_ip).first()
        if not device:
            device = Device.objects.filter(mac_address=source_mac).first()

        if device:
            IDSLog.objects.create(
                user=device.user,
                timestamp=timezone.now(),
                alert=log.get("alert"),
                source_ip=source_ip,
                destination_ip=destination_ip,
                source_mac=source_mac,
                destination_mac=destination_mac,
            )


# Example usage
parse_ids_logs("/path/to/ids/logs.json")
