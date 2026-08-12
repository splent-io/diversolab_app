# Content migration from diversolab.us.es (WordPress)

This directory keeps the frozen export of the old WordPress site so the news
import stays reproducible even after the old site goes offline.

- `wp_export/posts.json` contains the 82 published posts (title, slug, date,
  content, categories, featured image URL) in the interchange shape documented
  in `splent_feature_wordpress_import`.
- `wp_export/posts_draft.json` contains the 3 unpublished drafts, imported with
  draft status.

## How to run the import

The curated content (team, projects, tools, slider, partners, about, legal)
lives in feature seeders and is loaded by `splent db:seed`. The news archive is
imported by the WordPress importer feature:

```bash
# Preferred while the old site is online. Images are downloaded and inline
# URLs are rewritten to the local media library.
splent feature:wordpress_import posts --base-url https://diversolab.us.es
splent feature:wordpress_import posts --drafts-file migration/wp_export/posts_draft.json

# Offline fallback from this frozen export. Featured and inline images still
# resolve against their original URLs, so run it while they are reachable or
# restore a database dump instead.
splent feature:wordpress_import posts --file migration/wp_export/posts.json
```

The import is idempotent by post slug. After a successful import, take a
database dump (`splent db:dump`) so future environments can restore content
without depending on the old site.
