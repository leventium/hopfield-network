module hopfield
#(
    parameter MEM_WIDTH=16,
    parameter IMAGE_WIDTH=10,
    parameter PREDICT_EPOCHS=10
)
(
    input                                              clk,
    input                                              fit,
    input      [MEM_WIDTH*IMAGE_WIDTH*IMAGE_WIDTH-1:0] image,
    output reg [MEM_WIDTH*IMAGE_WIDTH*IMAGE_WIDTH-1:0] out
);
    localparam blank = { MEM_WIDTH {1'b0} };

    reg [MEM_WIDTH-1:0] mem [IMAGE_WIDTH*IMAGE_WIDTH-1:0][IMAGE_WIDTH*IMAGE_WIDTH-1:0];
    reg [MEM_WIDTH-1:0] tmp [IMAGE_WIDTH*IMAGE_WIDTH-1:0];
    integer i;
    integer j;
    integer k;


    initial begin
        for (i = 0; i < IMAGE_WIDTH*IMAGE_WIDTH; i = i + 1)
            for (j = 0; j < IMAGE_WIDTH*IMAGE_WIDTH; j = j + 1)
                mem[i][j] = blank;
        out = image;
    end


    always @(posedge clk) begin
        if (fit) begin
            for (i = 0; i < IMAGE_WIDTH*IMAGE_WIDTH; i = i + 1)
                for (j = 0; j < IMAGE_WIDTH*IMAGE_WIDTH; j = j + 1)
                    mem[i][j] = $signed(mem[i][j]) + $signed(image[MEM_WIDTH*(i+1)-1:MEM_WIDTH*i]) * $signed(image[MEM_WIDTH*(j+1)-1:MEM_WIDTH*j]);
        end else begin
            for (k = 0; k < PREDICT_EPOCHS; k = k + 1) begin
                for (i = 0; i < IMAGE_WIDTH*IMAGE_WIDTH; i = i + 1)
                    tmp[i] = { MEM_WIDTH {1'b0} };
                for (i = 0; i < IMAGE_WIDTH*IMAGE_WIDTH; i = i + 1) begin
                    for (j = 0; j < IMAGE_WIDTH*IMAGE_WIDTH; j = j + 1)
                        tmp[i] = $signed(tmp[i]) + $signed(mem[i][j]) * $signed(out[MEM_WIDTH*(j+1)-1:MEM_WIDTH*j]);
                    tmp[i] = ($signed(tmp[i]) >= 0) ? 1 : -1;
                end
                for (i = 0; i < IMAGE_WIDTH*IMAGE_WIDTH; i = i + 1)
                    out[MEM_WIDTH*(i+1)-1:MEM_WIDTH*i] = tmp[i];
            end
        end
    end

endmodule
