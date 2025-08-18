-- SurrealDB Schema for Marketing App
-- Using proper SurrealQL syntax

-- Organizations table
DEFINE TABLE organizations SCHEMAFULL;
DEFINE FIELD name ON TABLE organizations TYPE string ASSERT $value != NONE;
DEFINE FIELD description ON TABLE organizations TYPE string;
DEFINE FIELD website ON TABLE organizations TYPE string;
DEFINE FIELD email ON TABLE organizations TYPE string;
DEFINE FIELD phone ON TABLE organizations TYPE string;
DEFINE FIELD address ON TABLE organizations TYPE object;
DEFINE FIELD logo_url ON TABLE organizations TYPE string;
DEFINE FIELD settings ON TABLE organizations TYPE object;
DEFINE FIELD created_at ON TABLE organizations TYPE datetime DEFAULT time::now();
DEFINE FIELD updated_at ON TABLE organizations TYPE datetime DEFAULT time::now();
DEFINE FIELD status ON TABLE organizations TYPE string DEFAULT 'active';

-- Users table for organization members
DEFINE TABLE users SCHEMAFULL;
DEFINE FIELD email ON TABLE users TYPE string ASSERT $value != NONE;
DEFINE FIELD first_name ON TABLE users TYPE string ASSERT $value != NONE;
DEFINE FIELD last_name ON TABLE users TYPE string ASSERT $value != NONE;
DEFINE FIELD password_hash ON TABLE users TYPE string ASSERT $value != NONE;
DEFINE FIELD role ON TABLE users TYPE string DEFAULT 'member';
DEFINE FIELD avatar_url ON TABLE users TYPE string;
DEFINE FIELD last_login ON TABLE users TYPE datetime;
DEFINE FIELD created_at ON TABLE users TYPE datetime DEFAULT time::now();
DEFINE FIELD updated_at ON TABLE users TYPE datetime DEFAULT time::now();
DEFINE FIELD status ON TABLE users TYPE string DEFAULT 'active';

-- Media files (images/videos)
DEFINE TABLE media SCHEMAFULL;
DEFINE FIELD filename ON TABLE media TYPE string ASSERT $value != NONE;
DEFINE FIELD original_name ON TABLE media TYPE string ASSERT $value != NONE;
DEFINE FIELD file_url ON TABLE media TYPE string ASSERT $value != NONE;
DEFINE FIELD thumbnail_url ON TABLE media TYPE string;
DEFINE FIELD file_size ON TABLE media TYPE number;
DEFINE FIELD mime_type ON TABLE media TYPE string ASSERT $value != NONE;
DEFINE FIELD media_type ON TABLE media TYPE string ASSERT $value != NONE;
DEFINE FIELD dimensions ON TABLE media TYPE object;
DEFINE FIELD duration ON TABLE media TYPE number;
DEFINE FIELD alt_text ON TABLE media TYPE string;
DEFINE FIELD tags ON TABLE media TYPE array;
DEFINE FIELD metadata ON TABLE media TYPE object;
DEFINE FIELD created_at ON TABLE media TYPE datetime DEFAULT time::now();
DEFINE FIELD updated_at ON TABLE media TYPE datetime DEFAULT time::now();
DEFINE FIELD status ON TABLE media TYPE string DEFAULT 'active';

-- Advertisement campaigns
DEFINE TABLE advertisements SCHEMAFULL;
DEFINE FIELD title ON TABLE advertisements TYPE string ASSERT $value != NONE;
DEFINE FIELD description ON TABLE advertisements TYPE string;
DEFINE FIELD content ON TABLE advertisements TYPE string;
DEFINE FIELD ad_type ON TABLE advertisements TYPE string ASSERT $value != NONE;
DEFINE FIELD target_audience ON TABLE advertisements TYPE object;
DEFINE FIELD campaign_settings ON TABLE advertisements TYPE object;
DEFINE FIELD call_to_action ON TABLE advertisements TYPE object;
DEFINE FIELD tags ON TABLE advertisements TYPE array;
DEFINE FIELD created_at ON TABLE advertisements TYPE datetime DEFAULT time::now();
DEFINE FIELD updated_at ON TABLE advertisements TYPE datetime DEFAULT time::now();
DEFINE FIELD status ON TABLE advertisements TYPE string DEFAULT 'draft';

-- Email subscribers
DEFINE TABLE subscribers SCHEMAFULL;
DEFINE FIELD email ON TABLE subscribers TYPE string ASSERT $value != NONE;
DEFINE FIELD first_name ON TABLE subscribers TYPE string;
DEFINE FIELD last_name ON TABLE subscribers TYPE string;
DEFINE FIELD phone ON TABLE subscribers TYPE string;
DEFINE FIELD preferences ON TABLE subscribers TYPE object;
DEFINE FIELD demographics ON TABLE subscribers TYPE object;
DEFINE FIELD source ON TABLE subscribers TYPE string;
DEFINE FIELD subscribed_at ON TABLE subscribers TYPE datetime DEFAULT time::now();
DEFINE FIELD unsubscribed_at ON TABLE subscribers TYPE datetime;
DEFINE FIELD last_activity ON TABLE subscribers TYPE datetime;
DEFINE FIELD created_at ON TABLE subscribers TYPE datetime DEFAULT time::now();
DEFINE FIELD updated_at ON TABLE subscribers TYPE datetime DEFAULT time::now();
DEFINE FIELD status ON TABLE subscribers TYPE string DEFAULT 'active';

-- Email groups/segments
DEFINE TABLE email_groups SCHEMAFULL;
DEFINE FIELD name ON TABLE email_groups TYPE string ASSERT $value != NONE;
DEFINE FIELD description ON TABLE email_groups TYPE string;
DEFINE FIELD criteria ON TABLE email_groups TYPE object;
DEFINE FIELD tags ON TABLE email_groups TYPE array;
DEFINE FIELD created_at ON TABLE email_groups TYPE datetime DEFAULT time::now();
DEFINE FIELD updated_at ON TABLE email_groups TYPE datetime DEFAULT time::now();
DEFINE FIELD status ON TABLE email_groups TYPE string DEFAULT 'active';

-- Email campaigns/schedules
DEFINE TABLE email_campaigns SCHEMAFULL;
DEFINE FIELD name ON TABLE email_campaigns TYPE string ASSERT $value != NONE;
DEFINE FIELD subject ON TABLE email_campaigns TYPE string ASSERT $value != NONE;
DEFINE FIELD content ON TABLE email_campaigns TYPE string ASSERT $value != NONE;
DEFINE FIELD plain_text ON TABLE email_campaigns TYPE string;
DEFINE FIELD from_email ON TABLE email_campaigns TYPE string;
DEFINE FIELD from_name ON TABLE email_campaigns TYPE string;
DEFINE FIELD reply_to ON TABLE email_campaigns TYPE string;
DEFINE FIELD schedule_type ON TABLE email_campaigns TYPE string DEFAULT 'immediate';
DEFINE FIELD scheduled_at ON TABLE email_campaigns TYPE datetime;
DEFINE FIELD recurring_pattern ON TABLE email_campaigns TYPE object;
DEFINE FIELD stats ON TABLE email_campaigns TYPE object;
DEFINE FIELD created_at ON TABLE email_campaigns TYPE datetime DEFAULT time::now();
DEFINE FIELD updated_at ON TABLE email_campaigns TYPE datetime DEFAULT time::now();
DEFINE FIELD status ON TABLE email_campaigns TYPE string DEFAULT 'draft';

-- Organization topics/categories
DEFINE TABLE organization_topics SCHEMAFULL;
DEFINE FIELD name ON TABLE organization_topics TYPE string ASSERT $value != NONE;
DEFINE FIELD description ON TABLE organization_topics TYPE string;
DEFINE FIELD color ON TABLE organization_topics TYPE string;
DEFINE FIELD icon ON TABLE organization_topics TYPE string;
DEFINE FIELD created_at ON TABLE organization_topics TYPE datetime DEFAULT time::now();
DEFINE FIELD updated_at ON TABLE organization_topics TYPE datetime DEFAULT time::now();
DEFINE FIELD status ON TABLE organization_topics TYPE string DEFAULT 'active';

-- Define relationships using RELATE statements will be handled in the setup script
-- SurrealDB relationships are created when data is inserted with RELATE

-- Define indexes for better performance
DEFINE INDEX organizations_name ON TABLE organizations COLUMNS name;
DEFINE INDEX users_email ON TABLE users COLUMNS email UNIQUE;
DEFINE INDEX media_type ON TABLE media COLUMNS media_type;
DEFINE INDEX media_status ON TABLE media COLUMNS status;
DEFINE INDEX advertisements_status ON TABLE advertisements COLUMNS status;
DEFINE INDEX advertisements_type ON TABLE advertisements COLUMNS ad_type;
DEFINE INDEX subscribers_email ON TABLE subscribers COLUMNS email UNIQUE;
DEFINE INDEX subscribers_status ON TABLE subscribers COLUMNS status;
DEFINE INDEX email_campaigns_status ON TABLE email_campaigns COLUMNS status;
DEFINE INDEX email_campaigns_scheduled ON TABLE email_campaigns COLUMNS scheduled_at;
