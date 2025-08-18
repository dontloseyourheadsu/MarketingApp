#!/bin/bash
# SurrealDB Setup Script

set -e

echo "🚀 Marketing App - SurrealDB"
echo "============================"

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Navigate to database directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Start SurrealDB container
echo "🔄 Starting SurrealDB..."
if command -v docker-compose &> /dev/null; then
    docker-compose up -d
else
    docker compose up -d
fi

# Wait for SurrealDB to be ready
echo "🔄 Waiting for SurrealDB to be ready..."
for i in {1..30}; do
    if curl -s -f http://localhost:8000/health > /dev/null 2>&1; then
        echo "✅ SurrealDB is ready!"
        break
    fi
    
    if [ $i -eq 30 ]; then
        echo "❌ SurrealDB did not start in time"
        exit 1
    fi
    
    sleep 2
done

echo ""
echo "🎉 SurrealDB is running!"
echo ""
echo "Connection Info:"
echo "  URL: http://localhost:8000"
echo "  Username: root"
echo "  Password: root"
echo ""
echo "To stop: docker-compose down"
