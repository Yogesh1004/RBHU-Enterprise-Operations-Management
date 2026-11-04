/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        rbhu: {
          bg: "#0B1020",
          sidebar: "#111A2E",
          card: "#151F35",
          cardHover: "#1A2744",
          cardBorder: "#1E2C4A",
          border: "#1E293B",
          primary: "#6366F1",
          secondary: "#06B6D4",
          success: "#10B981",
          warning: "#F59E0B",
          danger: "#EF4444",
          text: "#F8FAFC",
          muted: "#94A3B8",
          dark: "#080C18",
        },
        primary: {
          DEFAULT: "#6366F1", // Indigo
          hover: "#4F46E5",
          dark: "#0B1020",
          card: "#151F35",
          sidebar: "#111A2E",
        },
        secondary: {
          DEFAULT: "#06B6D4", // Cyan
          hover: "#0891B2",
          light: "#E0F2FE",
        },
      },
      fontFamily: {
        sans: ["Inter", "-apple-system", "BlinkMacSystemFont", "Segoe UI", "Roboto", "sans-serif"],
      },
      boxShadow: {
        glow: "0 0 25px -5px rgba(99, 102, 241, 0.25)",
        cyanGlow: "0 0 25px -5px rgba(6, 182, 212, 0.25)",
      },
    },
  },
  plugins: [],
};
