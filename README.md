# Marketing App

A comprehensive application for managing marketing content, email campaigns, and advertising materials.

## Overview

This application provides marketing teams with tools to:

- Manage media content (images and videos)
- Create and maintain advertisements
- Manage email subscriber lists
- Send targeted ad campaigns to email subscribers
- Collaborate within marketing teams

## Documentation

- [Functional Requirements](docs/FUNCTIONAL_REQUIREMENTS.md) - Detailed requirements for all features
- [Technical Specifications](docs/TECHNICAL_SPECS.md) - Data models, API endpoints, and technical considerations

## Workflows

### A. Upload Ad & Send to Email

1. Marketing user uploads image/video
2. Creates an Ad associating media
3. Selects email group
4. Sends Ad → Email group receives content

### B. Team Collaboration

1. Admin creates a team
2. Adds marketing users
3. Team shares media/ad access

### C. [Future] Publish to Google Ads

1. OAuth2 connect Google Ads account
2. Select ad → publish/unpublish via API
