# How to Create a GitHub Release

The code and tag have been pushed to GitHub. Follow these steps to create a release:

## Option 1: Using GitHub Web Interface (Recommended)

1. **Go to your repository:**
   - Visit: https://github.com/rskworld/statistical-seaborn

2. **Navigate to Releases:**
   - Click on "Releases" in the right sidebar
   - Or go directly to: https://github.com/rskworld/statistical-seaborn/releases

3. **Create a New Release:**
   - Click "Draft a new release" button
   - Or if you see the tag v1.0.0, click "Create release from tag"

4. **Fill in Release Details:**
   - **Tag:** Select `v1.0.0` (should already exist)
   - **Release title:** `v1.0.0 - Statistical Data Analysis with Seaborn`
   - **Description:** Copy the content from `RELEASE_NOTES_v1.0.0.md`
   - **Target:** `main` branch
   - Check "Set as the latest release" if this is your first release

5. **Publish Release:**
   - Click "Publish release" button

## Option 2: Using GitHub CLI (if installed)

If you have GitHub CLI installed, you can run:

```bash
gh release create v1.0.0 --title "v1.0.0 - Statistical Data Analysis with Seaborn" --notes-file RELEASE_NOTES_v1.0.0.md
```

## Option 3: Using Git Commands

You can also create a release via the GitHub API, but the web interface is the easiest method.

## Release Notes Template

The release notes are already prepared in `RELEASE_NOTES_v1.0.0.md`. You can copy and paste this content into the GitHub release description field.

## What's Already Done

✅ Code pushed to GitHub  
✅ Tag v1.0.0 created and pushed  
✅ Release notes prepared  
⏳ Release creation (via GitHub web interface)

---

**Note:** The tag v1.0.0 has been successfully pushed to GitHub. You just need to create the release through the GitHub web interface to make it visible and downloadable.

