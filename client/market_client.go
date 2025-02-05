package main

import (
    "context"
    "fmt"
    "log"

    pb "path/to/market/proto"

    "google.golang.org/grpc"
)

func main() {
    conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure())
    if err != nil {
        log.Fatalf("Failed to connect to server: %v", err)
    }
    defer conn.Close()

    client := pb.NewMarketServiceClient(conn)

    resp, err := client.ListInstruments(context.Background(), &pb.Empty{})
    if err != nil {
        log.Fatalf("Error calling ListInstruments: %v", err)
    }

    fmt.Println("Available Instruments:")
    for _, instrument := range resp.Instruments {
        fmt.Printf("- %s: %s, $%.2f\n", instrument.Symbol, instrument.Type, instrument.Price)
    }
}
