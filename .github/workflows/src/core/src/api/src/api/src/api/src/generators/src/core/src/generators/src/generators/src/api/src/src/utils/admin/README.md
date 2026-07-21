# AI-Powered Automated Finance Blogging System 🚀

This is a complete, production-ready, hourly automated AI Finance Publisher using GitHub Actions, Blogger API, Gemini AI, and Supabase[span_18](start_span)[span_18](end_span).

## 🔒 Phase 25: Security Architecture
- **Zero Hardcoded Secrets**: All API keys, tokens, and DB credentials MUST be stored in GitHub Secrets[span_19](start_span)[span_19](end_span).
- **OAuth Scope**: The Blogger OAuth token only has access to post on the specific `BLOGGER_BLOG_ID`[span_20](start_span)[span_20](end_span).

## 🧪 Phase 26: Testing Instructions
Before deploying to production (GitHub Actions), test locally:
1. Copy `.env.example` to `.env` and fill in your keys.
2. Run `pip install -r requirements.txt`.
3. Run `python src/main.py`.
4. Check Blogger to verify the draft/post was created successfully.

## 🚀 Phase 27: Deployment to GitHub Actions

**Step 1: Push Code to GitHub**
Push this entire folder structure to a private GitHub repository.

**Step 2: Configure GitHub Secrets**
Go to Repository `Settings` > `Secrets and variables` > `Actions` > `New repository secret`[span_21](start_span)[span_21](end_span).
Add the following EXACT variables[span_22](start_span)[span_22](end_span):
* `BLOGGER_BLOG_ID`
* `GOOGLE_CLIENT_ID`
* `GOOGLE_CLIENT_SECRET`
* `GOOGLE_REFRESH_TOKEN`
* `GEMINI_TEXT_API_KEY`
* `GEMINI_IMAGE_API_KEY`
* `SUPABASE_URL`
* `SUPABASE_KEY`

**Step 3: Enable Workflows**
1. Go to the `Actions` tab in your repository.
2. Click `I understand my workflows, go ahead and enable them`.
3. The `Hourly Automated Finance Publisher` workflow will now run automatically every hour[span_23](start_span)[span_23](end_span).
4. To test immediately, click the workflow name and select **"Run workflow"** (Manual Dispatch)[span_24](start_span)[span_24](end_span).

## Concurrency and Duplicate Prevention
The `.github/workflows/hourly_publisher.yml` utilizes GitHub Actions `concurrency` groups[span_25](start_span)[span_25](end_span). If an hour takes longer than expected to generate content, the next job will queue or cancel, preventing duplicate posts on the exact same run[span_26](start_span)[span_26](end_span).

