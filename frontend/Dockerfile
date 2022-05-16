# =============================================================================
# Base
# =============================================================================
FROM node:lts-alpine AS base
RUN npm install -g http-server
WORKDIR /app
COPY package*.json ./

# =============================================================================
# Development
# =============================================================================
FROM base AS development
RUN npm install
COPY . .
RUN npm run build
CMD ["npm", "run", "serve", "--", "--port", "8002"]
# CMD [ "http-server", "dist" ]

# =============================================================================
# Production
# =============================================================================
FROM base AS production
RUN npm install
COPY . .
RUN npm run build
CMD ["npm", "run", "serve"]
# CMD [ "http-server", "dist" ]
