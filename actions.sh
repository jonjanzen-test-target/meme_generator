ORG="fairinternal"
gh repo list "$ORG" --limit 10 --json name | jq -r '.[].name' | while read REPO; do
  echo "Checking $ORG/$REPO"
  # List files in .github/workflows directory
  gh api repos/$ORG/$REPO/contents/.github/workflows --jq '.[] | .name' 2>/dev/null | while read FILE; do
    echo "  Found workflow file: $FILE"
    # Download the workflow file
    gh api repos/$ORG/$REPO/contents/.github/workflows/$FILE --jq '.download_url' | xargs curl -L -o "$ORG-$REPO-$FILE"
  done
done
