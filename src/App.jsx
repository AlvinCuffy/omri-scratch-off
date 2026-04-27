import { useState, useRef, useEffect } from “react”;
import { initializeApp } from “firebase/app”;
import { getFirestore, collection, addDoc, serverTimestamp } from “firebase/firestore”;

// ─── FIREBASE CONFIG ─────────────────────────────────
const firebaseConfig = {
apiKey: “AIzaSyBmhK6Avj0ZZHYxjEKkGUAv_K06zfT57eo”,
authDomain: “gen-lang-client-0807659054.firebaseapp.com”,
projectId: “gen-lang-client-0807659054”,
storageBucket: “gen-lang-client-0807659054.firebasestorage.app”,
messagingSenderId: “545794815177”,
appId: “1:545794815177:web:5092f702c2cb3522854918”
};

const firebaseApp = initializeApp(firebaseConfig);
const db = getFirestore(firebaseApp);

// ─── BRAND CONFIG ─────────────────────────────────────
// TO CUSTOMIZE PER CLIENT: change ONLY the values below
const BRAND = {
name: “KappaKuts Barbershop”,
tagline: “Where Greatness Is Personified”,
promo: “FREE Beard Trim”,
promoDetail: “with your next haircut — KappaKuts regulars only”,
expiry: “Valid at 10 Beaumaris Dr, Brampton · Expires May 31, 2026”,
confirmMsg: “Show this screen to your barber to redeem. Stay Frosty. 🔥”,
primaryColor: “#C9A84C”,
bg: “#0a0a0a”,
cardBg: “#111111”,
border: “#1e1e1e”,
// Firestore collection name — change per client so leads stay separate
leadsCollection: “kappakuts_leads”,
};
// ──────────────────────────────────────────────────────

// Save lead to Firestore
async function saveLead({ email, method, businessName }) {
try {
await addDoc(collection(db, BRAND.leadsCollection), {
email: email || null,
loginMethod: method,
business: businessName,
claimedAt: serverTimestamp(),
});
} catch (e) {
console.error(“Lead save error:”, e);
}
}

// ─── SCRATCH CARD ─────────────────────────────────────
function ScratchCard({ onWin }) {
const canvasRef = useRef(null);
const [scratching, setScratching] = useState(false);
const [won, setWon] = useState(false);
const [pct, setPct] = useState(0);

useEffect(() => {
const canvas = canvasRef.current;
if (!canvas) return;
const ctx = canvas.getContext(“2d”);
const dpr = window.devicePixelRatio || 1;
canvas.width = canvas.offsetWidth * dpr;
canvas.height = canvas.offsetHeight * dpr;
ctx.scale(dpr, dpr);

```
const w = canvas.offsetWidth;
const h = canvas.offsetHeight;

// Background gradient
const grad = ctx.createRadialGradient(w / 2, h / 2, 0, w / 2, h / 2, w / 1.2);
grad.addColorStop(0, "#2a2200");
grad.addColorStop(1, "#0f0f0f");
ctx.fillStyle = grad;
ctx.fillRect(0, 0, w, h);

// Gold burst lines
ctx.strokeStyle = "rgba(201,168,76,0.15)";
ctx.lineWidth = 1;
for (let i = 0; i < 28; i++) {
  const angle = (i / 28) * Math.PI * 2;
  ctx.beginPath();
  ctx.moveTo(w / 2, h / 2);
  ctx.lineTo(w / 2 + Math.cos(angle) * w, h / 2 + Math.sin(angle) * h);
  ctx.stroke();
}

// Scratch text
ctx.fillStyle = BRAND.primaryColor;
ctx.font = `bold ${w * 0.065}px system-ui`;
ctx.textAlign = "center";
ctx.textBaseline = "middle";
ctx.fillText("✦ SCRATCH HERE ✦", w / 2, h / 2 - 16);
ctx.font = `${w * 0.09}px serif`;
ctx.fillStyle = "rgba(201,168,76,0.6)";
ctx.fillText("✂", w / 2, h / 2 + 22);

ctx.globalCompositeOperation = "destination-out";
```

}, []);

const getXY = (e, canvas) => {
const rect = canvas.getBoundingClientRect();
const src = e.touches ? e.touches[0] : e;
return { x: src.clientX - rect.left, y: src.clientY - rect.top };
};

const doScratch = (e) => {
if (!scratching || won) return;
e.preventDefault();
const canvas = canvasRef.current;
const ctx = canvas.getContext(“2d”);
const dpr = window.devicePixelRatio || 1;
ctx.globalCompositeOperation = “destination-out”;
const { x, y } = getXY(e, canvas);
ctx.beginPath();
ctx.arc(x * dpr, y * dpr, 38 * dpr, 0, Math.PI * 2);
ctx.fill();

```
const data = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
let cleared = 0;
for (let i = 3; i < data.length; i += 4) if (data[i] < 128) cleared++;
const p = Math.round((cleared / (canvas.width * canvas.height)) * 100);
setPct(p);
if (p > 55 && !won) { setWon(true); onWin(); }
```

};

return (
<div style={{
position: “relative”, width: “100%”, height: 168,
borderRadius: 16, overflow: “hidden”,
border: `1px solid ${BRAND.border}`,
boxShadow: `0 0 40px rgba(201,168,76,0.08)`,
}}>
{/* Prize layer underneath */}
<div style={{
position: “absolute”, inset: 0,
background: “linear-gradient(135deg, #1a1200 0%, #0a0a0a 100%)”,
display: “flex”, flexDirection: “column”,
alignItems: “center”, justifyContent: “center”, gap: 6,
}}>
<div style={{ fontSize: 10, color: BRAND.primaryColor, letterSpacing: 3, textTransform: “uppercase”, fontWeight: 700 }}>
🎉 You Won
</div>
<div style={{ fontSize: 28, fontWeight: 900, color: “#fff”, letterSpacing: -0.5 }}>
{BRAND.promo}
</div>
<div style={{ fontSize: 12, color: “#666” }}>{BRAND.promoDetail}</div>
</div>

```
  {/* Scratch canvas */}
  <canvas
    ref={canvasRef}
    style={{
      position: "absolute", inset: 0, width: "100%", height: "100%",
      touchAction: "none", cursor: "crosshair",
    }}
    onMouseDown={() => setScratching(true)}
    onMouseUp={() => setScratching(false)}
    onMouseLeave={() => setScratching(false)}
    onMouseMove={doScratch}
    onTouchStart={(e) => { setScratching(true); doScratch(e); }}
    onTouchEnd={() => setScratching(false)}
    onTouchMove={doScratch}
  />

  {/* Progress hint */}
  {pct > 5 && pct < 55 && (
    <div style={{
      position: "absolute", bottom: 10, left: "50%", transform: "translateX(-50%)",
      background: "rgba(0,0,0,0.8)", color: BRAND.primaryColor,
      fontSize: 10, fontWeight: 700, padding: "4px 12px",
      borderRadius: 20, letterSpacing: 1, pointerEvents: "none",
    }}>
      {pct}% — KEEP SCRATCHING
    </div>
  )}
</div>
```

);
}

// ─── MAIN APP ─────────────────────────────────────────
export default function App() {
const [stage, setStage] = useState(“login”); // login | scratch | won
const [method, setMethod] = useState(null);
const [email, setEmail] = useState(””);
const [emailError, setEmailError] = useState(””);
const [saving, setSaving] = useState(false);

const S = {
page: {
minHeight: “100vh”,
background: BRAND.bg,
display: “flex”, alignItems: “center”, justifyContent: “center”,
padding: 20,
fontFamily: “‘DM Sans’, system-ui, sans-serif”,
},
card: {
width: “100%”, maxWidth: 360,
background: BRAND.cardBg,
borderRadius: 22,
border: `1px solid ${BRAND.border}`,
padding: “28px 24px”,
boxShadow: “0 24px 80px rgba(0,0,0,0.6)”,
},
btn: (bg, color, shadow) => ({
width: “100%”, padding: “14px 16px”,
background: bg, border: “none”, borderRadius: 12,
color, fontSize: 14, fontWeight: 700,
cursor: “pointer”, display: “flex”,
alignItems: “center”, justifyContent: “center”, gap: 10,
boxShadow: shadow || “none”,
transition: “opacity 0.15s”,
}),
label: {
fontSize: 10, color: BRAND.primaryColor,
letterSpacing: 3, textTransform: “uppercase”, fontWeight: 700,
},
divider: {
display: “flex”, alignItems: “center”, gap: 10, margin: “4px 0”,
},
line: { flex: 1, height: 1, background: BRAND.border },
};

const handleSocial = async (m) => {
setSaving(true);
setMethod(m);
await saveLead({ email: null, method: m, businessName: BRAND.name });
setSaving(false);
setStage(“scratch”);
};

const handleEmail = async () => {
if (!email.includes(”@”) || !email.includes(”.”)) {
setEmailError(“Enter a valid email to play.”);
return;
}
setSaving(true);
setMethod(“email”);
await saveLead({ email, method: “email”, businessName: BRAND.name });
setSaving(false);
setStage(“scratch”);
};

const handleWin = () => {
setTimeout(() => setStage(“won”), 600);
};

// ── LOGIN STAGE ──────────────────────────────────────
if (stage === “login”) return (
<div style={S.page}>
<div style={{ width: “100%”, maxWidth: 360, display: “flex”, flexDirection: “column”, alignItems: “center” }}>

```
    {/* Brand name header */}
    <div style={{ textAlign: "center", marginBottom: 24 }}>
      <div style={{ ...S.label, marginBottom: 10 }}>Exclusive Offer</div>
      <div style={{ fontSize: 26, fontWeight: 900, color: "#fff", letterSpacing: -0.5, lineHeight: 1.15, marginBottom: 6 }}>
        Scratch & Win<br />
        <span style={{ color: BRAND.primaryColor }}>{BRAND.promo}</span>
      </div>
      <div style={{ fontSize: 12, color: "#444", marginTop: 6 }}>
        Sign in to unlock your scratch card
      </div>
    </div>

    <div style={S.card}>
      {/* Facebook */}
      <button
        onClick={() => handleSocial("facebook")}
        disabled={saving}
        style={S.btn("#1877F2", "#fff")}
      >
        <svg width="18" height="18" viewBox="0 0 24 24" fill="white">
          <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z" />
        </svg>
        Continue with Facebook
      </button>

      <div style={{ height: 10 }} />

      {/* Google */}
      <button
        onClick={() => handleSocial("google")}
        disabled={saving}
        style={S.btn("#fff", "#222")}
      >
        <svg width="18" height="18" viewBox="0 0 24 24">
          <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" />
          <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" />
          <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z" />
          <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" />
        </svg>
        Sign in with Google
      </button>

      {/* Divider */}
      <div style={{ ...S.divider, margin: "16px 0" }}>
        <div style={S.line} />
        <div style={{ fontSize: 11, color: "#333", letterSpacing: 1 }}>OR</div>
        <div style={S.line} />
      </div>

      {/* Email */}
      <input
        type="email"
        placeholder="Enter your email"
        value={email}
        onChange={e => { setEmail(e.target.value); setEmailError(""); }}
        onKeyDown={e => e.key === "Enter" && handleEmail()}
        style={{
          width: "100%", padding: "13px 14px",
          background: "#1a1a1a",
          border: `1.5px solid ${emailError ? "#e53e3e" : "#2a2a2a"}`,
          borderRadius: 12, color: "#fff", fontSize: 14,
          outline: "none", boxSizing: "border-box",
          fontFamily: "inherit", marginBottom: emailError ? 6 : 10,
        }}
      />
      {emailError && (
        <div style={{ fontSize: 11, color: "#e53e3e", marginBottom: 8 }}>
          {emailError}
        </div>
      )}

      <button
        onClick={handleEmail}
        disabled={saving}
        style={S.btn(
          BRAND.primaryColor, "#0a0a0a",
          `0 4px 24px ${BRAND.primaryColor}55`
        )}
      >
        {saving ? "LOADING..." : "▶ PLAY NOW"}
      </button>

      <div style={{ fontSize: 10, color: "#2a2a2a", textAlign: "center", marginTop: 14, lineHeight: 1.6 }}>
        By playing you agree to receive promotional messages from {BRAND.name}.
        Your info is never sold.
      </div>
    </div>

    <div style={{ marginTop: 20, fontSize: 10, color: "#1e1e1e", letterSpacing: 2, textTransform: "uppercase" }}>
      Digital Scratch-Offs by Omri Media
    </div>
  </div>
</div>
```

);

// ── SCRATCH STAGE ────────────────────────────────────
if (stage === “scratch”) return (
<div style={S.page}>
<div style={{ width: “100%”, maxWidth: 360 }}>

```
    <div style={{ textAlign: "center", marginBottom: 20 }}>
      <div style={{ fontSize: 22, fontWeight: 900, color: "#fff", letterSpacing: -0.5, marginBottom: 4 }}>
        {BRAND.name}
      </div>
      <div style={{ fontSize: 12, color: "#444" }}>{BRAND.tagline}</div>
    </div>

    <div style={S.card}>
      <div style={{ textAlign: "center", marginBottom: 18 }}>
        <div style={{ ...S.label, marginBottom: 8 }}>🎉 You're in — now scratch</div>
        <div style={{ fontSize: 18, fontWeight: 900, color: "#fff", marginBottom: 4 }}>
          Reveal your exclusive prize
        </div>
        <div style={{ fontSize: 12, color: "#444" }}>
          Use your finger to scratch below
        </div>
      </div>

      <ScratchCard onWin={handleWin} />

      <div style={{ textAlign: "center", marginTop: 14, fontSize: 11, color: "#2a2a2a" }}>
        {BRAND.expiry}
      </div>
    </div>

    <div style={{ textAlign: "center", marginTop: 20, fontSize: 10, color: "#1e1e1e", letterSpacing: 2, textTransform: "uppercase" }}>
      Digital Scratch-Offs by Omri Media
    </div>
  </div>
</div>
```

);

// ── WON STAGE ────────────────────────────────────────
return (
<div style={S.page}>
<div style={{ width: “100%”, maxWidth: 360 }}>

```
    <div style={{ textAlign: "center", marginBottom: 20 }}>
      <div style={{ fontSize: 22, fontWeight: 900, color: "#fff", letterSpacing: -0.5, marginBottom: 4 }}>
        {BRAND.name}
      </div>
      <div style={{ fontSize: 12, color: "#444" }}>{BRAND.tagline}</div>
    </div>

    <div style={S.card}>
      <div style={{ textAlign: "center" }}>
        <div style={{ fontSize: 52, marginBottom: 12 }}>🏆</div>
        <div style={{ ...S.label, marginBottom: 8 }}>Congratulations</div>
        <div style={{ fontSize: 30, fontWeight: 900, color: "#fff", letterSpacing: -0.5, marginBottom: 6 }}>
          {BRAND.promo}
        </div>
        <div style={{ fontSize: 13, color: "#555", marginBottom: 24 }}>
          {BRAND.promoDetail}
        </div>

        {/* Prize card */}
        <div style={{
          background: "linear-gradient(135deg, #1a1200 0%, #0f0f0f 100%)",
          border: `2px dashed ${BRAND.primaryColor}`,
          borderRadius: 16, padding: "22px 20px", marginBottom: 18,
        }}>
          <div style={{ fontSize: 10, color: "#444", letterSpacing: 2, textTransform: "uppercase", marginBottom: 8 }}>
            Your Prize
          </div>
          <div style={{ fontSize: 26, fontWeight: 900, color: BRAND.primaryColor, marginBottom: 4 }}>
            {BRAND.promo}
          </div>
          <div style={{ fontSize: 12, color: "#555" }}>{BRAND.promoDetail}</div>
        </div>

        {/* Redeem message */}
        <div style={{
          background: "#0f0f0f", border: `1px solid ${BRAND.border}`,
          borderRadius: 12, padding: "14px 16px", marginBottom: 16,
          fontSize: 14, color: "#F5F0E8", lineHeight: 1.6,
        }}>
          {BRAND.confirmMsg}
        </div>

        <div style={{ fontSize: 11, color: "#2a2a2a" }}>{BRAND.expiry}</div>

        <div style={{
          marginTop: 22, paddingTop: 16,
          borderTop: `1px solid ${BRAND.border}`,
          fontSize: 10, color: "#1e1e1e",
          letterSpacing: 2, textTransform: "uppercase",
        }}>
          Digital Scratch-Offs by Omri Media
        </div>
      </div>
    </div>
  </div>
</div>
```

);
}
