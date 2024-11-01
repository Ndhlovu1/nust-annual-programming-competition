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

**UML DIAGRAM BASED ON THE ABOVE CLASSES**

![Screenshot from 2024-11-01 16-00-20](https://github.com/user-attachments/assets/c84a6b54-4d27-48dc-a975-5bf72f546347)

## PROBLEM SOLVING AND ANALYSIS

**User Registration and Authentication: A secure system for participants, judges, and organizers to create accounts and manage their profiles.
Problem Submission and Evaluation: A robust platform for participants to submit their code Steps Taken in Brainstorming Stages:**

1. Ideation Sessions:
    Encouraged team members to contribute ideas freely, without judgment.
    Conducted regular brainstorming sessions both in-person and online.
    Used tools like whiteboards, sticky notes, and online collaboration platforms to capture and organize ideas.
2. Mind Mapping:
    Created visual mind maps to explore the relationships and connections between ideas.
    Identified key themes and patterns that emerged from the brainstorming sessions.
    Used mind maps to identify potential solutions and areas for further exploration.
3.  SWOT Analysis:
    Evaluated the software's strengths, weaknesses, opportunities, and threats.
    Conducted a competitive analysis to identify potential advantages and disadvantages.
    Used SWOT analysis to make informed decisions about the software's features and design.
    
### User Stories
We created user stories from the perspective of different stakeholders (participants, judges, organizers).
Used user stories to understand the needs, goals, and pain points of each stakeholder group.
Incorporated user stories into the design process to ensure the software meets their requirements.User Stories

1. As a Participant, I want to be able to:
    Register for the competition and create a profile.
    View past competitions and their results.
    Submit my code for evaluation.
    View the real-time leaderboard and my ranking.
    Collaborate with other participants using the platform's communication tools.
    Receive feedback and scores from judges.

2. As a Judge, I want to be able to:
    Create an account and manage my profile.
    Evaluate participant submissions and provide feedback.
    Assign scores to participants based on their performance.
    View the real-time leaderboard and analyze participant rankings.
    Communicate with other judges using the platform's collaboration tools.

3. As an Organizer, I want to be able to:
    Create and manage the competition schedule, rules, and announcements.
    Broadcast messages to all users or selected groups of users.
    Manage participant registrations and deregistrations.
    View reports and analytics on competition participation and performance.
    Collaborate with other organizers using the platform's communication tools.

4. As a Sponsor, I want to be able to:
    Create an account and manage my profile.
    View information about the competition and its participants.
    Contact organizers and participants through the platform's communication tools.
    Promote my sponsorship and interact with the competition community.

5. As a Volunteer, I want to be able to:
    Create an account and manage my profile.
    View information about the competition and its schedule.
    Register for volunteer opportunities and manage my availability.
    Communicate with organizers and other volunteers using the platform's communication tools.

### PROTOTYPING 

We developed several paper sketches that allowed for the application's user interface to be easily developed
**PROJECT PAPER SKETCHES**

![WhatsApp Image 2024-11-01 at 16 08 43](https://github.com/user-attachments/assets/471dad53-d473-4b02-94f6-f489374e8ed6)

![WhatsApp Image 2024-11-01 at 16 08 42](https://github.com/user-attachments/assets/0fe20c61-4bca-4a47-9825-62c8d690875d)

![WhatsApp Image 2024-11-01 at 16 08 42 (1)](https://github.com/user-attachments/assets/9805b663-bfbb-44f0-8f0e-0a6c25f5ea78)

![WhatsApp Image 2024-11-01 at 16 08 42](https://github.com/user-attachments/assets/6d3009bc-92d0-47d3-ac41-4a72c8803d13)
























