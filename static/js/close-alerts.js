function closeAlerts(alertClass, timeout) {
    setTimeout(function () {
        var alerts = document.querySelectorAll('.' + alertClass);
        alerts.forEach(function (alert) {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, timeout);
}

document.addEventListener('DOMContentLoaded', function () {
   
});