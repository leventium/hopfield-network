module rom #(
    parameter MEM_WIDTH = 16,
    parameter IMAGE_WIDTH = 10,
    parameter MAX_SIZE = 9
)
(
    input                                              clk,
    input      [7:0]                                   a,
    output reg [MEM_WIDTH*IMAGE_WIDTH*IMAGE_WIDTH-1:0] image
);
    reg [MEM_WIDTH*IMAGE_WIDTH*IMAGE_WIDTH-1:0] mem [MAX_SIZE-1:0];
    assign image = mem[a];

    initial begin
        $readmemh("data.hex", mem);
    end

endmodule
