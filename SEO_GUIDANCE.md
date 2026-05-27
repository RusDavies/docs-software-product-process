# SEO Guidance for Web Products

SEO for web products should be designed in from product framing through release. Search visibility, share previews, crawlability, performance, information architecture, and durable content are product requirements, not garnish applied after launch by someone muttering at a sitemap.

## Purpose

This guidance applies to web projects where public discovery, indexed content, social sharing, enterprise trust pages, documentation discoverability, or long-term organic reach matters.

It covers:

- SEO goals and audience intent
- keyword/topic strategy
- information architecture
- metadata and structured data
- crawlability and indexability
- technical SEO
- performance and Core Web Vitals
- content quality and freshness
- analytics and privacy-safe measurement
- launch and post-launch SEO checks

## When This Applies

Use this guidance for:

- marketing websites
- public documentation sites
- blogs/news/tutorial sites
- product landing pages
- SaaS/application public pages
- ecommerce/catalog-style pages
- enterprise trust/security/compliance pages
- knowledge bases and support sites
- any public web property expected to be found, understood, shared, or indexed

For private/internal-only web apps, use only the parts relevant to share previews, accessibility, performance, and user-facing content.

## Minimum Expectations

At minimum, define:

1. SEO/discovery goals
2. target audiences and search intent
3. priority topics/pages
4. URL and information architecture
5. metadata requirements
6. indexability/crawlability expectations
7. sitemap/robots/canonical approach
8. structured data needs, where relevant
9. performance/Core Web Vitals expectations
10. analytics/search-console measurement plan
11. launch SEO QA checklist
12. content maintenance owner/cadence

## Full SEO Checklist

### 1. SEO Goals and Audience Intent

Capture:

- business/product goals
- target audiences
- search intent by audience
- priority conversion or success actions
- geographic/language targeting where relevant
- branded vs non-branded search expectations
- competitor/comparable sites
- success metrics

### 2. Topic and Keyword Strategy

Define:

- primary topics
- supporting topics
- target queries or query clusters
- user vocabulary
- content gaps
- internal-link opportunities
- pages that should not target search

Avoid keyword stuffing. Search engines and humans both dislike being beaten with a thesaurus.

### 3. Information Architecture and URL Design

Design:

- logical page hierarchy
- readable URLs
- canonical URL patterns
- navigation labels
- breadcrumbs where useful
- hub/spoke topic organization
- pagination/filter behavior
- archive/category/tag strategy

URLs should be stable, descriptive, and boring. Boring URLs age better than clever ones.

### 4. Metadata and Share Previews

Specify for each indexable page type:

- title pattern
- meta description pattern
- canonical URL
- Open Graph title/description/image
- Twitter/X card metadata where relevant
- robots meta behavior
- language/locale metadata
- favicon/app icons where relevant

### 5. Structured Data

Use structured data where it honestly represents page content.

Possible schema types:

- Organization
- WebSite
- WebPage
- Article / BlogPosting
- FAQPage
- HowTo
- Product
- SoftwareApplication
- BreadcrumbList
- Person
- Event

Validate structured data before release. Do not add fake FAQ or review markup because some SEO blog from 2017 made bad choices sound profitable.

### 6. Crawlability and Indexability

Define:

- robots.txt behavior
- XML sitemap generation
- sitemap submission path
- canonicalization
- redirects
- noindex/nofollow rules
- handling of duplicate/filter/search pages
- 404/410 behavior
- staging/private environment indexing protections

### 7. Technical SEO

Verify:

- semantic HTML structure
- one clear H1 per page where appropriate
- heading hierarchy
- internal links are crawlable
- links use descriptive anchor text
- images have useful alt text where appropriate
- lazy loading does not hide critical content
- client-side rendering does not block indexing unexpectedly
- redirects are intentional
- status codes are correct
- mobile rendering works

### 8. Performance and Core Web Vitals

Plan for:

- fast first load
- Largest Contentful Paint (LCP)
- Interaction to Next Paint (INP)
- Cumulative Layout Shift (CLS)
- image optimization
- font loading
- script budgets
- cache strategy
- CDN/static asset strategy where relevant

Performance is both UX and SEO. Also, slow websites are a tiny distributed denial-of-service attack on patience.

### 9. Content Quality and Maintenance

Define:

- content owner
- review cadence
- freshness expectations
- author/reviewer attribution where useful
- expertise/trust signals
- update/deprecation process
- broken-link review
- archive/removal process
- editorial style and tone

For trust-sensitive products, avoid claims the product cannot support. This overlaps with documentation, compliance, and governance.

### 10. Accessibility and SEO Alignment

Ensure:

- meaningful page titles
- logical headings
- descriptive links
- alt text
- readable content structure
- keyboard-accessible navigation
- caption/transcript needs for media

Accessibility is not an SEO hack. It is a baseline quality requirement that also keeps search crawlers from needing a Ouija board.

### 11. Analytics and Search Measurement

Define:

- analytics tool(s)
- privacy posture and consent requirements
- Search Console/Bing Webmaster setup where relevant
- key events/conversions
- dashboard/report cadence
- query/page monitoring
- index coverage monitoring
- Core Web Vitals monitoring

Measurement should be privacy-aware and proportionate.

### 12. Launch SEO QA

Before launch, verify:

- intended pages are indexable
- private/staging pages are not indexable
- titles/descriptions are present and sensible
- canonical links are correct
- sitemap exists and is valid
- robots.txt is correct
- structured data validates
- Open Graph/share previews work
- redirects work
- 404 page works
- mobile rendering works
- performance checks pass or exceptions are approved
- analytics/Search Console setup is ready where relevant

### 13. Post-Launch SEO Review

After launch, review:

- index coverage
- crawl errors
- sitemap ingestion
- performance/Core Web Vitals
- search queries and impressions
- broken links
- top entry pages
- conversion/support outcomes
- content gaps
- pages needing updates

Turn findings into backlog items.

## Lightweight Web Project Version

For small web projects:

1. target audience and top search intents
2. page list and URL plan
3. title/meta description patterns
4. Open Graph/share preview plan
5. sitemap/robots/canonical checks
6. basic performance/accessibility checks
7. analytics/Search Console decision
8. launch SEO smoke test

## Recommended Project Files

- `docs/seo/seo-plan.md`
- `docs/seo/page-inventory.md`
- `docs/seo/metadata-plan.md`
- `docs/seo/technical-seo-checklist.md`
- `docs/seo/launch-seo-checklist.md`
- `docs/seo/post-launch-seo-review.md`

## Definition of SEO-Ready

A web project is SEO-ready when:

- SEO/discovery goals are defined
- target audience and search intent are understood
- page inventory and URL structure are planned
- metadata and indexability expectations are known
- technical SEO requirements are included in implementation work
- analytics/search measurement decisions are made
- SEO QA is part of release readiness

## Definition of SEO-Done

SEO is done when:

- priority pages have correct metadata
- crawl/index controls are correct
- sitemap/robots/canonical behavior is correct
- structured data validates where used
- performance/accessibility basics are checked
- launch SEO QA passes or exceptions are approved
- post-launch review is scheduled
- SEO follow-up items are in the backlog
