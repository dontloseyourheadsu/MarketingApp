# 📦 Media Storage Architecture

## Amazon S3 Storage Strategy

- Primary storage in Amazon S3 buckets with region-based sharding
- Object naming convention: `{team_id}/{type}/{uuid}.{extension}`
- Versioning enabled for media overwrite protection
- Server-side encryption (SSE-S3) for data-at-rest protection

## CloudFront CDN Integration

- CloudFront distribution for cached global delivery
- Edge location optimization for low-latency access
- Signed URLs for time-limited secure access to assets
- Custom domain with SSL certificate

## Upload Flow

1. Client requests pre-signed S3 URL from API
2. Direct browser-to-S3 upload using pre-signed URL
3. API validates and registers upload once complete
4. CDN invalidation for updated assets when necessary

## Media Validation

- Size limits: Images (10MB), Videos (200MB)
- Supported formats:
  - Images: JPEG, PNG, WebP, SVG
  - Videos: MP4, WebM
- Malware/virus scanning prior to acceptance
- Metadata extraction (dimensions, duration, etc.)

## Deduplication Strategy

- Content-based hashing for exact duplicate detection
- Perceptual hashing for near-duplicate images
- Option to reference existing media or create new copy

## Lifecycle Policies

- Unused draft media auto-deleted after 30 days
- Archival tier for media from completed campaigns (90+ days old)
- Permanent deletion requires confirmed team approval
