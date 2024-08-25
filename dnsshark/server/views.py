from django.shortcuts import render, redirect
from .models import DomainRule
from django.contrib.auth.decorators import login_required
import subprocess
from django.shortcuts import render, redirect
from .models import DomainRule
from django.contrib.auth.decorators import login_required
import subprocess


@login_required
def dashboard_view(request):
    if request.method == "POST":
        domain = request.POST.get("domain")
        action = request.POST.get("action")
        DomainRule.objects.create(user=request.user, domain=domain, action=action)
        update_unbound_config()
        return redirect("dashboard")

    rules = DomainRule.objects.filter(user=request.user)
    return render(request, "server/dashboard.html", {"rules": rules})


def update_unbound_config():
    rules = DomainRule.objects.all()
    config_lines = []

    for rule in rules:
        if rule.action == "block":
            config_lines.append(f'local-zone: "{rule.domain}" static')

    config_path = "/etc/unbound/unbound.conf.d/blocked_domains.conf"

    with open(config_path, "w") as config_file:
        config_file.write("\n".join(config_lines))

    subprocess.run(["sudo", "systemctl", "restart", "unbound"])


@login_required
def dashboard_view(request):
    if request.method == "POST":
        domain = request.POST.get("domain")
        action = request.POST.get("action")
        DomainRule.objects.create(user=request.user, domain=domain, action=action)
        update_unbound_config()
        return redirect("dashboard")

    rules = DomainRule.objects.filter(user=request.user)
    return render(request, "server/dashboard.html", {"rules": rules})


def update_unbound_config():
    rules = DomainRule.objects.all()
    config_lines = []

    for rule in rules:
        if rule.action == "block":
            config_lines.append(f'local-zone: "{rule.domain}" static')

    config_path = "/etc/unbound/unbound.conf.d/blocked_domains.conf"

    with open(config_path, "w") as config_file:
        config_file.write("\n".join(config_lines))

    subprocess.run(["sudo", "systemctl", "restart", "unbound"])
