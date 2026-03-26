from django.db import models
import shortuuid


class Appointment(models.Model):
    id = models.CharField(primary_key=True, max_length=22, default=shortuuid.uuid, editable=False, unique=True)
    client = models.ForeignKey("clients.Client", on_delete=models.CASCADE, related_name="appointments")
    enterprise = models.ForeignKey("enterprise.Enterprise", on_delete=models.CASCADE, related_name="appointments")
    service = models.ForeignKey("services.Services", on_delete=models.CASCADE, related_name="appointments")
    scheduled_at = models.DateTimeField()
    observation = models.TextField(max_length=200, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("SCHEDULED", "Scheduled"),
            ("COMPLETED", "Completed"),
            ("CANCELLED", "Cancelled"),
        ],
        default="SCHEDULED",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Appointment {self.client} - {self.scheduled_at.strftime('%Y-%m-%d %H:%M')}"
    