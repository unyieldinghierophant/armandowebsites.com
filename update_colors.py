import re

with open('index.html', 'r') as f:
    content = f.read()

# Variables mapping
replacements = [
    (r'--bg:\s*#080808;', '--bg:      #0B0D10;'),
    (r'--surface:\s*#0f0f0f;', '--surface: #1A1D21;'),
    (r'--text:\s*#f0ede8;', '--text:    #E6E8EB;'),
    (r'--muted:\s*rgba\(240,237,232,0\.38\);', '--muted:   #A6A9AD;'),
    (r'--accent:\s*#d4f060;', '--accent:  #FF6A00;'),
    (r'--accent2:\s*#b8d94e;', '--accent2: #FF8C2A;'),
    
    # Hex and RGB occurrences
    (r'#d4f060', '#FF6A00'),
    (r'#b8d94e', '#FF8C2A'),
    (r'212,240,96', '255,106,0'),
    (r'#a8e040', '#FF8C2A'),
    
    (r'#080808', '#0B0D10'),
    (r'8,8,8', '11,13,16'),
    
    (r'#0f0f0f', '#1A1D21'),
    (r'15,15,15', '26,29,33'),
    
    (r'#f0ede8', '#E6E8EB'),
    (r'240,237,232', '230,232,235'),
    
    # Specific elements
    (r'border: 1px solid rgba\(255,255,255,0\.07\);', 'border: 1px solid rgba(166,169,173,0.15);'),
    (r'--border:\s*rgba\(255,255,255,0\.07\);', '--border:  rgba(166,169,173,0.15);')
]

for old, new in replacements:
    content = re.sub(old, new, content, flags=re.IGNORECASE)

# Update button primary
btn_primary_old = r"""\.btn-primary \{.*?\}"""
btn_primary_new = """.btn-primary {
    display: inline-flex; align-items: center; gap: 10px;
    background: #1A1D21; color: #FF6A00;
    border: 1px solid #A6A9AD;
    font-family: var(--font-body); font-size: 14px;
    font-weight: 700; letter-spacing: .06em; text-transform: uppercase;
    padding: 16px 33px; border-radius: 4px; text-decoration: none;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.05);
    transition: background .2s, border-color .2s, color .2s, transform .2s;
  }
  .btn-primary:hover {
    background: #FF6A00; color: #0B0D10; border-color: #FF6A00;
    transform: translateY(-2px);
  }
  .btn-primary svg { width: 18px; height: 18px; fill: currentColor; }"""
content = re.sub(r'\.btn-primary\s*\{[^}]+\}\s*\.btn-primary:hover\s*\{[^}]+\}\s*\.btn-primary svg\s*\{[^}]+\}', btn_primary_new, content, flags=re.DOTALL)

# Update button ghost
btn_ghost_old = r"""\.btn-ghost \{.*?\}"""
btn_ghost_new = """.btn-ghost {
    display: inline-flex; align-items: center; gap: 8px;
    background: transparent; color: #A6A9AD;
    border: 1px solid #A6A9AD;
    font-size: 14px; font-weight: 600;
    letter-spacing: .06em; text-transform: uppercase;
    text-decoration: none; padding: 16px 27px; border-radius: 4px;
    box-shadow: inset 0 0 10px rgba(166,169,173,0.05);
    transition: background .3s, color .3s, border-color .3s, transform .2s;
  }
  .btn-ghost:hover {
    background: #A6A9AD; color: #0B0D10;
    transform: translateY(-2px);
  }"""
content = re.sub(r'\.btn-ghost\s*\{[^}]+\}\s*\.btn-ghost:hover\s*\{[^}]+\}', btn_ghost_new, content, flags=re.DOTALL)

# Update CTA specific
cta_btn_old = r"""\.cta-btn-dark\s*\{[^}]+\}\s*\.cta-btn-dark:hover\s*\{[^}]+\}\s*\.cta-btn-dark svg\s*\{[^}]+\}"""
cta_btn_new = """.cta-btn-dark {
  display: inline-flex; align-items: center; gap: 10px;
  background: #1A1D21; color: #FF6A00; border: 1px solid #FF6A00;
  font-family: var(--font-body); font-size: 14px;
  font-weight: 700; letter-spacing: .08em; text-transform: uppercase;
  padding: 18px 36px; border-radius: 4px; text-decoration: none;
  box-shadow: inset 0 1px 5px rgba(255,106,0,0.1);
  transition: transform .2s, background .2s, color .2s;
}
.cta-btn-dark:hover {
  background: #FF6A00; color: #0B0D10;
  transform: translateY(-2px);
}
.cta-btn-dark svg { width: 18px; height: 18px; fill: currentColor; }"""
content = re.sub(cta_btn_old, cta_btn_new, content, flags=re.DOTALL)

# Pricing cards
# Change radius
content = content.replace('border-radius: 20px', 'border-radius: 4px')
content = content.replace('border-radius: 100px', 'border-radius: 4px')

with open('index_modified.html', 'w') as f:
    f.write(content)
