package main

import (
    "context"
    "log"
    "net"
    "sync"

    pb "path/to/analytics/proto"

    "google.golang.org/grpc"
)

type server struct {
    pb.UnimplementedAnalyticsServiceServer
    priceData  map[string][]float64
    volumeData map[string][]float64
    mutex      sync.Mutex
}

func (s *server) GetPriceSummary(ctx context.Context, req *pb.Symbol) (*pb.PriceSummary, error) {
    s.mutex.Lock()
    defer s.mutex.Unlock()
    prices, exists := s.priceData[req.Symbol]
    if !exists {
        return nil, fmt.Errorf("Symbol not found")
    }
    avg := 0.0
    min, max := prices[0], prices[0]
    for _, price := range prices {
        avg += price
        if price > max {
            max = price
        }
        if price < min {
            min = price
        }
    }
    avg /= float64(len(prices))
    return &pb.PriceSummary{
        Symbol:       req.Symbol,
        AveragePrice: avg,
        HighestPrice: max,
        LowestPrice:  min,
    }, nil
}

func (s *server) GetVolumeTrends(ctx context.Context, req *pb.Symbol) (*pb.VolumeTrends, error) {
    s.mutex.Lock()
    defer s.mutex.Unlock()
    volumes, exists := s.volumeData[req.Symbol]
    if !exists {
        return nil, fmt.Errorf("Symbol not found")
    }
    return &pb.VolumeTrends{Symbol: req.Symbol, Volumes: volumes}, nil
}

func main() {
    listener, err := net.Listen("tcp", ":50052")
    if err != nil {
        log.Fatalf("Failed to listen on port 50052: %v", err)
    }
    grpcServer := grpc.NewServer()
    pb.RegisterAnalyticsServiceServer(grpcServer, &server{
        priceData:  make(map[string][]float64),
        volumeData: make(map[string][]float64),
    })
    log.Println("Analytics server is running on port 50052")
    if err := grpcServer.Serve(listener); err != nil {
        log.Fatalf("Failed to serve: %v", err)
    }
}
