package main

import (
    "context"
    "log"
    "net"
    "sync"

    pb "path/to/market/proto"

    "google.golang.org/grpc"
)

type server struct {
    pb.UnimplementedMarketServiceServer
    instruments map[string]*pb.Instrument
    orderBook   map[string][]*pb.Order
    mutex       sync.Mutex
}

func (s *server) AddInstrument(ctx context.Context, req *pb.Instrument) (*pb.Response, error) {
    s.mutex.Lock()
    defer s.mutex.Unlock()
    s.instruments[req.Symbol] = req
    return &pb.Response{Success: true, Message: "Instrument added successfully"}, nil
}

func (s *server) ListInstruments(ctx context.Context, req *pb.Empty) (*pb.InstrumentList, error) {
    s.mutex.Lock()
    defer s.mutex.Unlock()
    var instruments []*pb.Instrument
    for _, instrument := range s.instruments {
        instruments = append(instruments, instrument)
    }
    return &pb.InstrumentList{Instruments: instruments}, nil
}

func (s *server) PlaceOrder(ctx context.Context, req *pb.Order) (*pb.Response, error) {
    s.mutex.Lock()
    defer s.mutex.Unlock()
    s.orderBook[req.Symbol] = append(s.orderBook[req.Symbol], req)
    return &pb.Response{Success: true, Message: "Order placed successfully"}, nil
}

func (s *server) QueryOrderBook(ctx context.Context, req *pb.Symbol) (*pb.OrderBook, error) {
    s.mutex.Lock()
    defer s.mutex.Unlock()
    orders := s.orderBook[req.Symbol]
    var buyOrders, sellOrders []*pb.Order
    for _, order := range orders {
        if order.Type == "buy" {
            buyOrders = append(buyOrders, order)
        } else {
            sellOrders = append(sellOrders, order)
        }
    }
    return &pb.OrderBook{Symbol: req.Symbol, BuyOrders: buyOrders, SellOrders: sellOrders}, nil
}

func main() {
    listener, err := net.Listen("tcp", ":50051")
    if err != nil {
        log.Fatalf("Failed to listen on port 50051: %v", err)
    }
    grpcServer := grpc.NewServer()
    pb.RegisterMarketServiceServer(grpcServer, &server{
        instruments: make(map[string]*pb.Instrument),
        orderBook:   make(map[string][]*pb.Order),
    })
    log.Println("Market server is running on port 50051")
    if err := grpcServer.Serve(listener); err != nil {
        log.Fatalf("Failed to serve: %v", err)
    }
}
