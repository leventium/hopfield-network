`timescale 1 ns / 100 ps

module testbench;

    parameter T = 100;

    reg clk;
    wire [9:0] res;

    top t (
        .clk        ( clk ),
        .image_part ( res )
    );

    initial begin
        clk = 0;
        forever clk = #(T/2) ~clk;
    end

    integer cycle; initial cycle = 0;

    always @(posedge clk) begin
        $write("%5d res = %b\n", cycle, res);
    end

endmodule
