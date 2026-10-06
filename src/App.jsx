import React, { useState, useRef, useEffect } from 'react';
import { 
  Play, Pause, Volume2, VolumeX, RotateCcw, Download, Mic, 
  Upload, CheckCircle2, AlertTriangle, FileText, Send, ShieldCheck, 
  ExternalLink, Sparkles, Radio, BookmarkCheck, ArrowRight, Clock, Award,
  Sliders, Copy, Check, RefreshCw, Users, PhoneCall, CheckSquare, Plus, Trash2, Camera, Layers
} from 'lucide-react';

export default function App() {
  const [activeTab, setActiveTab] = useState('greenscreen'); // Default to greenscreen to showcase the new framework
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(20.17);
  const [isMuted, setIsMuted] = useState(false);
  const [copiedIndex, setCopiedIndex] = useState(null);
  const videoRef = useRef(null);

  // Outreach & 8 PM Call Tracker State
  const [contacts, setContacts] = useState(() => {
    const saved = localStorage.getItem('ghw_daily_contacts');
    if (saved) {
      try { return JSON.parse(saved); } catch (e) {}
    }
    return [
      { id: 1, name: "Prospect 1 (Hot Interest)", type: "Warm Market", status: "Follow-Up Needed", notes: "Watched call yesterday. Send: 'What did you like best?'", phone: "" },
      { id: 2, name: "Mom", type: "Warm Market", status: "Follow-Up Needed", notes: "Watched call last night to support. Send positive check-in.", phone: "" },
      { id: 3, name: "Attendee 3", type: "Warm Market", status: "Follow-Up Needed", notes: "Attended yesterday's 8 PM call.", phone: "" },
      { id: 4, name: "Attendee 4", type: "Warm Market", status: "Follow-Up Needed", notes: "Attended yesterday's 8 PM call.", phone: "" },
      { id: 5, name: "Attendee 5", type: "Warm Market", status: "Follow-Up Needed", notes: "Attended yesterday's 8 PM call.", phone: "" },
      { id: 6, name: "", type: "New Outreach", status: "To Invite", notes: "Call today for tonight's 8 PM Zoom.", phone: "" },
      { id: 7, name: "", type: "New Outreach", status: "To Invite", notes: "Call today for tonight's 8 PM Zoom.", phone: "" },
      { id: 8, name: "", type: "New Outreach", status: "To Invite", notes: "Call today for tonight's 8 PM Zoom.", phone: "" },
      { id: 9, name: "", type: "New Outreach", status: "To Invite", notes: "Call today for tonight's 8 PM Zoom.", phone: "" },
      { id: 10, name: "", type: "New Outreach", status: "To Invite", notes: "Call today for tonight's 8 PM Zoom.", phone: "" },
    ];
  });

  const [newName, setNewName] = useState('');
  const [newType, setNewType] = useState('Warm Market');

  useEffect(() => {
    localStorage.setItem('ghw_daily_contacts', JSON.stringify(contacts));
  }, [contacts]);

  const updateContact = (id, field, value) => {
    setContacts(contacts.map(c => c.id === id ? { ...c, [field]: value } : c));
  };

  const addContact = () => {
    if (!newName.trim()) return;
    const newEntry = {
      id: Date.now(),
      name: newName.trim(),
      type: newType,
      status: "To Invite",
      notes: "Invited for 8 PM call.",
      phone: ""
    };
    setContacts([...contacts, newEntry]);
    setNewName('');
  };

  const removeContact = (id) => {
    setContacts(contacts.filter(c => c.id !== id));
  };

  const confirmedTonight = contacts.filter(c => c.status === 'Confirmed 8 PM' || c.status === 'Attended').length;

  const handleCopyText = (text, idx) => {
    navigator.clipboard.writeText(text);
    setCopiedIndex(idx);
    setTimeout(() => setCopiedIndex(null), 2000);
  };

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#090d16', color: '#f8fafc', fontFamily: 'system-ui, -apple-system, sans-serif' }}>
      
      {/* Top Header */}
      <header style={{ borderBottom: '1px solid #1e293b', backgroundColor: '#0d1322', padding: '16px 24px' }}>
        <div style={{ maxWidth: '1400px', margin: '0 auto', display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '16px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
            <div style={{ width: '42px', height: '42px', borderRadius: '10px', backgroundColor: '#f59e0b', display: 'flex', alignItems: 'center', justifyContent: 'center', boxShadow: '0 0 20px rgba(245, 158, 11, 0.4)' }}>
              <ShieldCheck size={26} color="#000" />
            </div>
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <h1 style={{ fontSize: '18px', fontWeight: '800', letterSpacing: '-0.02em', margin: 0, color: '#ffffff' }}>
                  THE GOLDEN HORSESHOE REPORT • STUDIO
                </h1>
                <span style={{ backgroundColor: '#1e293b', border: '1px solid #334155', color: '#10b981', fontSize: '11px', fontWeight: '700', padding: '2px 8px', borderRadius: '999px', textTransform: 'uppercase' }}>
                  Green Screen & Borrowed Authority
                </span>
              </div>
              <p style={{ margin: 0, fontSize: '12px', color: '#94a3b8' }}>
                Alvin Cuffy • Instagram Reel & TikTok Authority Engine (@goldenhorseshoewatch)
              </p>
            </div>
          </div>

          {/* Navigation Tabs */}
          <nav style={{ display: 'flex', gap: '8px', backgroundColor: '#1e293b', padding: '4px', borderRadius: '12px' }}>
            <button 
              onClick={() => setActiveTab('greenscreen')}
              style={{
                display: 'flex', alignItems: 'center', gap: '6px',
                padding: '8px 16px', borderRadius: '8px', fontSize: '13px', fontWeight: '700',
                border: 'none', cursor: 'pointer', transition: 'all 0.2s',
                backgroundColor: activeTab === 'greenscreen' ? '#f59e0b' : 'transparent',
                color: activeTab === 'greenscreen' ? '#000000' : '#94a3b8'
              }}
            >
              <Camera size={15} /> Green Screen Reels (New!)
            </button>
            <button 
              onClick={() => setActiveTab('tracker')}
              style={{
                display: 'flex', alignItems: 'center', gap: '6px',
                padding: '8px 16px', borderRadius: '8px', fontSize: '13px', fontWeight: '600',
                border: 'none', cursor: 'pointer', transition: 'all 0.2s',
                backgroundColor: activeTab === 'tracker' ? '#10b981' : 'transparent',
                color: activeTab === 'tracker' ? '#ffffff' : '#94a3b8'
              }}
            >
              <Users size={15} /> 10-Guest Tracker
            </button>
            <button 
              onClick={() => setActiveTab('studio')}
              style={{
                display: 'flex', alignItems: 'center', gap: '6px',
                padding: '8px 16px', borderRadius: '8px', fontSize: '13px', fontWeight: '600',
                border: 'none', cursor: 'pointer', transition: 'all 0.2s',
                backgroundColor: activeTab === 'studio' ? '#3b82f6' : 'transparent',
                color: activeTab === 'studio' ? '#ffffff' : '#94a3b8'
              }}
            >
              <Play size={15} /> Form N4 Video
            </button>
            <button 
              onClick={() => setActiveTab('funnel')}
              style={{
                display: 'flex', alignItems: 'center', gap: '6px',
                padding: '8px 16px', borderRadius: '8px', fontSize: '13px', fontWeight: '600',
                border: 'none', cursor: 'pointer', transition: 'all 0.2s',
                backgroundColor: activeTab === 'funnel' ? '#3b82f6' : 'transparent',
                color: activeTab === 'funnel' ? '#ffffff' : '#94a3b8'
              }}
            >
              <Send size={15} /> DM Scripts
            </button>
          </nav>
        </div>
      </header>

      {/* Main Studio Body */}
      <main style={{ maxWidth: '1400px', margin: '0 auto', padding: '24px 16px' }}>
        
        {/* TAB: GREEN SCREEN REELS ENGINE */}
        {activeTab === 'greenscreen' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '28px' }}>
            
            {/* Strategy Explainer Banner */}
            <div style={{ backgroundColor: '#0f172a', borderRadius: '20px', border: '1px solid #1e293b', padding: '24px 28px' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '14px', marginBottom: '12px' }}>
                <div style={{ width: '44px', height: '44px', borderRadius: '12px', backgroundColor: '#f59e0b', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                  <Layers size={24} color="#000" />
                </div>
                <div>
                  <h2 style={{ fontSize: '20px', fontWeight: '800', margin: 0, color: '#ffffff' }}>
                    Alvin Cuffy Green Screen "Borrowed Authority" Framework
                  </h2>
                  <p style={{ margin: 0, fontSize: '13px', color: '#94a3b8' }}>
                    Positioning you as the trusted local watchdog pointing directly at official Ontario e-Laws statutes
                  </p>
                </div>
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '16px', marginTop: '16px' }}>
                <div style={{ backgroundColor: '#0d1322', borderRadius: '12px', border: '1px solid #1e293b', padding: '16px' }}>
                  <span style={{ fontSize: '11px', fontWeight: '800', color: '#f59e0b' }}>1. THE BACKGROUND</span>
                  <p style={{ margin: '6px 0 0 0', fontSize: '13px', color: '#cbd5e1' }}>Official <code style={{ color: '#38bdf8' }}>ontario.ca</code> government document with clean bullet points and statutory citations.</p>
                </div>
                <div style={{ backgroundColor: '#0d1322', borderRadius: '12px', border: '1px solid #1e293b', padding: '16px' }}>
                  <span style={{ fontSize: '11px', fontWeight: '800', color: '#10b981' }}>2. THE FOREGROUND</span>
                  <p style={{ margin: '6px 0 0 0', fontSize: '13px', color: '#cbd5e1' }}>You in the lower-third, pointing directly up/left at the exact clause as you explain it.</p>
                </div>
                <div style={{ backgroundColor: '#0d1322', borderRadius: '12px', border: '1px solid #1e293b', padding: '16px' }}>
                  <span style={{ fontSize: '11px', fontWeight: '800', color: '#3b82f6' }}>3. THE CONVERSION</span>
                  <p style={{ margin: '6px 0 0 0', fontSize: '13px', color: '#cbd5e1' }}>Call out a DM keyword ("ENTRY" / "CHECKLIST") to drive hot prospects into private 1-on-1 chats.</p>
                </div>
              </div>
            </div>

            {/* Template 1 & 2 Cards */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(440px, 1fr))', gap: '24px' }}>
              
              {/* Template 1: Unannounced Entry */}
              <div style={{ backgroundColor: '#0f172a', borderRadius: '20px', border: '1px solid #1e293b', padding: '24px', display: 'flex', flexDirection: 'column', gap: '16px' }}>
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                  <span style={{ fontSize: '12px', fontWeight: '800', backgroundColor: '#3b82f6', color: '#fff', padding: '4px 10px', borderRadius: '6px' }}>
                    TEMPLATE 1 • TENANT RIGHTS (RTA S. 27)
                  </span>
                  <a 
                    href="/media/greenscreen_template_unannounced_entry.png" 
                    download="greenscreen_template_unannounced_entry.png"
                    style={{ backgroundColor: '#10b981', color: '#fff', textDecoration: 'none', padding: '6px 12px', borderRadius: '6px', fontSize: '12px', fontWeight: '700', display: 'flex', alignItems: 'center', gap: '6px' }}
                  >
                    <Download size={14} /> Download 1080x1920
                  </a>
                </div>

                <div style={{ width: '100%', aspectRatio: '9/16', backgroundColor: '#000', borderRadius: '12px', overflow: 'hidden', border: '1px solid #334155' }}>
                  <img src="/media/greenscreen_template_unannounced_entry.png" alt="Unannounced Entry Green Screen" style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
                </div>

                {/* Teleprompter & Camera Cues */}
                <div style={{ backgroundColor: '#0d1322', borderRadius: '12px', border: '1px solid #1e293b', padding: '16px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
                    <span style={{ fontSize: '12px', fontWeight: '800', color: '#f59e0b' }}>35-SECOND GREEN SCREEN SCRIPT:</span>
                    <button 
                      onClick={() => handleCopyText("Your landlord just walked into your unit unannounced? Here's what the law actually says in Ontario. Under Section 27 of the Residential Tenancies Act, your landlord MUST give you 24 hours written notice before entering. The notice must state the exact reason and a time between 8 AM and 8 PM. The ONLY exception is a genuine emergency like a flood or fire. If your landlord enters illegally, they face fines up to $50,000. If you're dealing with illegal entries or landlord harassment in the GTA, DM me the word 'ENTRY' for our free Ontario tenant rights guide.", 201)}
                      style={{ backgroundColor: copiedIndex === 201 ? '#10b981' : '#1e293b', border: '1px solid #334155', color: '#fff', padding: '4px 8px', borderRadius: '6px', fontSize: '11px', fontWeight: '700', cursor: 'pointer' }}
                    >
                      {copiedIndex === 201 ? 'Copied!' : 'Copy Script'}
                    </button>
                  </div>
                  <p style={{ margin: 0, fontSize: '13px', color: '#cbd5e1', lineHeight: '1.6' }}>
                    <strong style={{ color: '#38bdf8' }}>[0:00 - Point UP 👆]:</strong> "Your landlord just walked into your unit unannounced? Here's what the law actually says in Ontario.<br/>
                    <strong style={{ color: '#f59e0b' }}>[0:08 - Point to Notice Bullet]:</strong> Under Section 27 of the Residential Tenancies Act, your landlord MUST give you 24 hours written notice before entering. The notice must state the exact reason and a time between 8 AM and 8 PM.<br/>
                    <strong style={{ color: '#ef4444' }}>[0:20 - Point to Red Box]:</strong> The ONLY exception is a genuine emergency like a flood or fire.<br/>
                    <strong style={{ color: '#10b981' }}>[0:28 - Look directly into camera]:</strong> If you're dealing with illegal landlord entries in the GTA, DM me the word <strong>'ENTRY'</strong> for our free Ontario tenant rights guide."
                  </p>
                </div>
              </div>

              {/* Template 2: Why Are You Still A Landlord? */}
              <div style={{ backgroundColor: '#0f172a', borderRadius: '20px', border: '1px solid #1e293b', padding: '24px', display: 'flex', flexDirection: 'column', gap: '16px' }}>
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                  <span style={{ fontSize: '12px', fontWeight: '800', backgroundColor: '#ef4444', color: '#fff', padding: '4px 10px', borderRadius: '6px' }}>
                    TEMPLATE 2 • LANDLORD TENSION (RTA S. 59)
                  </span>
                  <a 
                    href="/media/greenscreen_template_why_still_landlord.png" 
                    download="greenscreen_template_why_still_landlord.png"
                    style={{ backgroundColor: '#10b981', color: '#fff', textDecoration: 'none', padding: '6px 12px', borderRadius: '6px', fontSize: '12px', fontWeight: '700', display: 'flex', alignItems: 'center', gap: '6px' }}
                  >
                    <Download size={14} /> Download 1080x1920
                  </a>
                </div>

                <div style={{ width: '100%', aspectRatio: '9/16', backgroundColor: '#000', borderRadius: '12px', overflow: 'hidden', border: '1px solid #334155' }}>
                  <img src="/media/greenscreen_template_why_still_landlord.png" alt="Why Still Landlord Green Screen" style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
                </div>

                {/* Teleprompter & Camera Cues */}
                <div style={{ backgroundColor: '#0d1322', borderRadius: '12px', border: '1px solid #1e293b', padding: '16px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
                    <span style={{ fontSize: '12px', fontWeight: '800', color: '#ef4444' }}>40-SECOND GREEN SCREEN SCRIPT:</span>
                    <button 
                      onClick={() => handleCopyText("Ontario landlords... why are you still doing this? With everything going on across Brampton, Mississauga, and Toronto, why would anyone willingly be a landlord in this province right now? Look at the math: average LTB delay is 8 to 10 months. Even if your tenant owes $60,000, the tribunal maximum is capped at $35,000. And if you make one single calendar error on your N4 notice, your case is thrown out on day one. If you're currently holding rental property in Ontario, what is your actual game plan? Drop your thoughts below or DM me 'CHECKLIST' for our free pre-filing audit guide.", 202)}
                      style={{ backgroundColor: copiedIndex === 202 ? '#10b981' : '#1e293b', border: '1px solid #334155', color: '#fff', padding: '4px 8px', borderRadius: '6px', fontSize: '11px', fontWeight: '700', cursor: 'pointer' }}
                    >
                      {copiedIndex === 202 ? 'Copied!' : 'Copy Script'}
                    </button>
                  </div>
                  <p style={{ margin: 0, fontSize: '13px', color: '#cbd5e1', lineHeight: '1.6' }}>
                    <strong style={{ color: '#ef4444' }}>[0:00 - Hands to Head / Shocked]:</strong> "Ontario landlords... why are you still doing this? With everything going on across Brampton, Mississauga, and Toronto, why would anyone willingly be a landlord in this province right now?<br/>
                    <strong style={{ color: '#f59e0b' }}>[0:12 - Point to Stats]:</strong> Look at the math: average LTB delay is 8 to 10 months. Even if your tenant owes $60,000, the tribunal maximum is capped at $35,000.<br/>
                    <strong style={{ color: '#38bdf8' }}>[0:24 - Point to Fatal Defect]:</strong> And if you make one single calendar error on your N4 notice, your case is thrown out on day one.<br/>
                    <strong style={{ color: '#10b981' }}>[0:32 - Call to Action]:</strong> If you're holding rental property in Ontario, what's your plan? Drop your thoughts below or DM me <strong>'CHECKLIST'</strong> to join our nightly landlord strategy overview."
                  </p>
                </div>
              </div>

            </div>

            {/* How to Film on Phone Instructions */}
            <div style={{ backgroundColor: '#0d1322', borderRadius: '16px', border: '1px solid #1e293b', padding: '20px' }}>
              <h3 style={{ fontSize: '15px', fontWeight: '800', margin: '0 0 10px 0', color: '#10b981' }}>
                📱 How to Record This in 3 Minutes on Instagram / TikTok / CapCut:
              </h3>
              <ol style={{ margin: 0, paddingLeft: '20px', fontSize: '13px', color: '#cbd5e1', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                <li>Click <strong>"Download 1080x1920"</strong> on either template above and save the image to your phone's photo gallery.</li>
                <li>Open **Instagram Reels** or **TikTok** → tap **Effects / Filters** → select **"Green Screen"**.</li>
                <li>Choose the downloaded document template as your background photo.</li>
                <li>Stand in the bottom-right or bottom-center (just like your reference photos), hit record, and read the script while pointing at the bullet points!</li>
              </ol>
            </div>

          </div>
        )}

        {/* TAB: TRACKER */}
        {activeTab === 'tracker' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '16px' }}>
              <div style={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', borderRadius: '16px', padding: '20px' }}>
                <span style={{ fontSize: '12px', fontWeight: '700', color: '#94a3b8', textTransform: 'uppercase' }}>Tonight's 8:00 PM Goal</span>
                <div style={{ display: 'flex', alignItems: 'baseline', gap: '8px', marginTop: '6px' }}>
                  <span style={{ fontSize: '32px', fontWeight: '900', color: '#10b981' }}>{confirmedTonight}</span>
                  <span style={{ fontSize: '18px', color: '#64748b', fontWeight: '700' }}>/ 10 Confirmed</span>
                </div>
                <div style={{ marginTop: '12px', width: '100%', height: '8px', backgroundColor: '#1e293b', borderRadius: '999px', overflow: 'hidden' }}>
                  <div style={{ width: `${Math.min((confirmedTonight / 10) * 100, 100)}%`, height: '100%', backgroundColor: '#10b981' }}></div>
                </div>
              </div>
              <div style={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', borderRadius: '16px', padding: '20px' }}>
                <span style={{ fontSize: '12px', fontWeight: '700', color: '#94a3b8', textTransform: 'uppercase' }}>Daily Window</span>
                <div style={{ display: 'flex', alignItems: 'baseline', gap: '8px', marginTop: '6px' }}>
                  <span style={{ fontSize: '24px', fontWeight: '900', color: '#f59e0b' }}>10:00 AM – 3:00 PM</span>
                </div>
                <p style={{ margin: '8px 0 0 0', fontSize: '12px', color: '#cbd5e1' }}>5 Hours: Reachouts → Content → Follow-ups → Confirmations.</p>
              </div>
            </div>

            <div style={{ backgroundColor: '#0f172a', borderRadius: '16px', border: '1px solid #1e293b', padding: '20px' }}>
              <h3 style={{ fontSize: '16px', fontWeight: '800', margin: '0 0 16px 0', color: '#ffffff' }}>Active Contacts & Follow-ups</h3>
              <div style={{ overflowX: 'auto' }}>
                <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '13px' }}>
                  <thead>
                    <tr style={{ borderBottom: '1px solid #1e293b', color: '#94a3b8' }}>
                      <th style={{ padding: '10px 12px' }}>#</th>
                      <th style={{ padding: '10px 12px' }}>Name</th>
                      <th style={{ padding: '10px 12px' }}>Type</th>
                      <th style={{ padding: '10px 12px' }}>Status</th>
                      <th style={{ padding: '10px 12px' }}>Notes</th>
                    </tr>
                  </thead>
                  <tbody>
                    {contacts.map((c, index) => (
                      <tr key={c.id} style={{ borderBottom: '1px solid #1e293b' }}>
                        <td style={{ padding: '12px', color: '#64748b', fontWeight: '700' }}>{index + 1}</td>
                        <td style={{ padding: '12px', fontWeight: '600' }}>{c.name || "Enter Name..."}</td>
                        <td style={{ padding: '12px' }}><span style={{ fontSize: '11px', fontWeight: '700', backgroundColor: '#1e293b', padding: '3px 8px', borderRadius: '4px' }}>{c.type}</span></td>
                        <td style={{ padding: '12px' }}>
                          <span style={{ fontSize: '11px', fontWeight: '700', backgroundColor: c.status === 'Confirmed 8 PM' ? '#10b981' : '#f59e0b', color: '#000', padding: '3px 8px', borderRadius: '4px' }}>
                            {c.status}
                          </span>
                        </td>
                        <td style={{ padding: '12px', color: '#94a3b8' }}>{c.notes}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        )}

        {/* TAB: STUDIO */}
        {activeTab === 'studio' && (
          <div style={{ display: 'grid', gridTemplateColumns: 'minmax(320px, 420px) 1fr', gap: '28px', alignItems: 'start' }}>
            <div style={{ backgroundColor: '#0f172a', borderRadius: '20px', border: '1px solid #1e293b', padding: '16px' }}>
              <video
                ref={videoRef}
                src="/media/ontario_n4_calendar_trap_reel.mp4"
                playsInline
                onTimeUpdate={() => { if (videoRef.current) setCurrentTime(videoRef.current.currentTime); }}
                style={{ width: '100%', aspectRatio: '9/16', objectFit: 'contain', backgroundColor: '#000', borderRadius: '16px' }}
              />
            </div>
          </div>
        )}

        {/* TAB: FUNNEL */}
        {activeTab === 'funnel' && (
          <div style={{ maxWidth: '850px', margin: '0 auto' }}>
            <div style={{ backgroundColor: '#0f172a', borderRadius: '20px', border: '1px solid #1e293b', padding: '28px' }}>
              <h2 style={{ fontSize: '20px', fontWeight: '800', margin: '0 0 16px 0', color: '#ffffff' }}>Inbound DM "CHECKLIST" Conversion Blueprint</h2>
              <p style={{ color: '#94a3b8', fontSize: '14px' }}>"Hey! Here is the direct link to the Ontario LTB Pre-Filing Checklist. Quick question: are you currently dealing with a non-payment situation right now?"</p>
            </div>
          </div>
        )}

      </main>
    </div>
  );
}
