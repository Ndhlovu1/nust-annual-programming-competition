# events/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def email_attendees(self):
        attendees = self.rsvp_set.values_list('user__email', flat=True)
        message = f"""
        <html>
            <body>
                <h2>Good day,</h2>
                <h2>This is your reminder to attend the {self.title}</h2>
                
                <h2><b>Date & Time : {self.date}</b></h2>
                <h2><b>Location : {self.location}</b></h2>
                <h2>Event Details :</h2>
                <p>{self.description}</p>
                <p><b>Kindly pass all enquiries/cancellations to prg.competition@gmail.com</b></p>
            </body>
        </html>
        """
        send_mail(
            subject=f"Update for {self.title}",
            message=message,
            from_email="tinomudaishendhlovu@gmail.com",
            recipient_list=attendees,
            html_message=message,
        )


class RSVP(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'user')  # Prevents duplicate RSVPs for the same event

    def __str__(self):
        return f"{self.user.username} RSVP for {self.event.title}"

