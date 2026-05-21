#!/bin/bash
set -e
echo "📦 Building mdBook site..."
mdbook build
echo "✅ Build complete. Output: site/"
