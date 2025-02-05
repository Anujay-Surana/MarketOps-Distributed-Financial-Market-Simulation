FROM golang:1.18 as builder
WORKDIR /app
COPY . .
RUN go mod tidy
RUN go build -o market_server ./server/market_server.go
RUN go build -o analytics_server ./server/analytics_server.go

# Final Image
FROM alpine:latest
WORKDIR /root/
COPY --from=builder /app/market_server .
COPY --from=builder /app/analytics_server .
EXPOSE 50051 50052
CMD ["./market_server"]
