<template>
    <div class="container">
      <canvas ref="canvas" @mousedown="startDrawing" @mouseup="stopDrawing" @mousemove="draw"></canvas>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isDrawing: false,
        context: null,
        centerX: 0,
        centerY: 0,
        rotationAngle: 0,
        animationFrame: null,
        lastX: 0,
        lastY: 0,
      };
    },
    mounted() {
      const canvas = this.$refs.canvas;
      canvas.width = 500;
      canvas.height = 500;
      this.context = canvas.getContext('2d');
      this.centerX = canvas.width / 2;
      this.centerY = canvas.height / 2;
      this.startSpinning();
    },
    beforeUnmount() {
      cancelAnimationFrame(this.animationFrame);
    },
    methods: {
      startSpinning() {
        const drawFrame = () => {
          this.rotationAngle += 1;
          if (this.rotationAngle >= 360) {
            this.rotationAngle = 0;
          }
  
          this.context.clearRect(0, 0, this.$refs.canvas.width, this.$refs.canvas.height);
          this.context.save();
          this.context.translate(this.centerX, this.centerY);
          this.context.rotate((this.rotationAngle * Math.PI) / 180);
          this.context.translate(-this.centerX, -this.centerY);
  
          this.context.beginPath();
          this.context.arc(this.centerX, this.centerY, 100, 0, Math.PI * 2);
          this.context.stroke();
  
          this.context.restore();
  
          if (this.isDrawing) {
            this.context.save();
            this.context.translate(this.centerX, this.centerY);
            this.context.rotate((this.rotationAngle * Math.PI) / 180);
            this.context.translate(-this.centerX, -this.centerY);
  
            this.context.lineTo(this.lastX, this.lastY);
            this.context.stroke();
  
            this.context.restore();
          }
  
          this.animationFrame = requestAnimationFrame(drawFrame);
        };
        drawFrame();
      },
      startDrawing(event) {
        this.isDrawing = true;
        this.lastX = event.offsetX;
        this.lastY = event.offsetY;
        this.context.beginPath();
        this.context.moveTo(this.lastX, this.lastY);
      },
      stopDrawing() {
        this.isDrawing = false;
        this.context.closePath();
      },
      draw(event) {
        if (!this.isDrawing) return;
        this.lastX = event.offsetX;
        this.lastY = event.offsetY;
      },
    },
  };
  </script>
  
  <style scoped>
  .container {
    position: relative;
    width: 500px;
    height: 500px;
  }
  canvas {
    border: 1px solid black;
  }
  </style>
  