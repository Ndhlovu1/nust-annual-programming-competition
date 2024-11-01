# Nust Annual Programming Competition - Software Documentation

This document outlines the software project for the Nust Annual Programming Competition, detailing its features and the brainstorming methodologies in place to facilitate its development.

## Project Overview
The Nust Annual Programming Competition is a prestigious event that aims to foster a spirit of innovation and problem-solving among students. The software platform supporting this competition will be designed to provide a seamless and engaging experience for participants, judges, and organizers.

## Key Features

1. Home
2. Events
3. Gallery
4. Announcements
5. Forum
6. Archives : Allows for sharing past document and other amazing alternatives
7. Polls : Allows for collecting data from the participants on any suggested changes
8. Mentorship : Allows for people to request for a mentor and apply for a mentorship position
9. Messaging : Allows for in-app communication
10. Emailing : SMTP server setup for live communication
11. Admin Interface for managing the profile
12. Authentication and Authorization
13. Taggit Manager : Used for managing 

## Informative Breakdown

Classes:

    HomePage: Represents the homepage.
        Attributes: title, content
        Methods: display_content()

    Event: Manages events, allowing users to RSVP.
        Attributes: title, date, location, description
        Methods: create_event(), edit_event(), delete_event(), register_user()

    Gallery: Holds media files for display in the gallery.
        Attributes: image, caption
        Methods: upload_image(), delete_image(), display_gallery()

    Announcement: Manages announcements for the platform.
        Attributes: title, date, content
        Methods: add_announcement(), update_announcement(), delete_announcement()

    Forum: Manages forum discussions.
        Attributes: topic, content, created_at
        Methods: create_topic(), post_reply()

    Archive: Handles archived documents.
        Attributes: title, document_file, description
        Methods: add_document(), delete_document(), view_document()

    Poll: Represents polls for feedback.
        Attributes: question, options, deadline
        Methods: create_poll(), vote(), close_poll()

    Mentorship: Manages mentorship requests and mentor applications.
        Attributes: requestor, mentor, request_date, status
        Methods: request_mentor(), apply_for_mentor(), approve_application()

    Messaging: Manages in-app messages.
        Attributes: sender, receiver, message_content, timestamp
        Methods: send_message(), delete_message()

    Email: Handles SMTP configurations for emailing.
        Attributes: smtp_host, smtp_port, email_address, password
        Methods: send_email()

    AdminInterface: Provides functionalities for admin-level profile management.
        Attributes: admin_id, permissions
        Methods: manage_profile(), grant_permissions()

    Authentication: Manages login, logout, and user registration.
        Attributes: username, password, roles
        Methods: login(), logout(), register(), authorize()

    TagManager (from taggit): Manages tags for content categorization.
        Attributes: tag_name, content_type
        Methods: add_tag(), remove_tag(), list_tags()





