# =============================================================================
# Base
# =============================================================================
FROM node:lts-alpine AS base
WORKDIR /app
COPY package*.json ./

# =============================================================================
# Development
# =============================================================================
FROM base AS development
RUN npm install -g @vue/cli && npm install
# RUN npm install
COPY . .
CMD [ "npm", "run", "serve", "--", "--port", "8002" ]

# =============================================================================
# Production
# =============================================================================
FROM base AS production
RUN npm install -g http-server && npm install
COPY . .
RUN npm run build
CMD [ "http-server", "dist" ]
