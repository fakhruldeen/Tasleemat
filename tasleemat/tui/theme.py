"""
tasleemat.tui.theme
CSS styles, color tokens, and visual layout definitions for the Tasleemat TUI.
"""

TUI_CSS = """
Screen {
    background: #0f172a;
    color: #f8fafc;
}

Header {
    background: #1e293b;
    color: #38bdf8;
    dock: top;
    height: 3;
}

Footer {
    background: #1e293b;
    color: #94a3b8;
    dock: bottom;
    height: 1;
}

#header_container {
    height: 3;
    background: #1e293b;
    border-bottom: heavy #006a61;
    layout: horizontal;
    padding: 0 1;
}

#header_title {
    width: 60%;
    text-style: bold;
    color: #38bdf8;
    content-align: left middle;
}

#header_meta {
    width: 40%;
    color: #94a3b8;
    content-align: right middle;
}

Tabs {
    background: #0f172a;
    border-bottom: solid #334155;
}

Tab {
    padding: 0 2;
    color: #94a3b8;
}

Tab.-active {
    color: #38bdf8;
    text-style: bold;
    background: #1e293b;
    border-bottom: tall #006a61;
}

.panel-container {
    padding: 1 2;
    height: 1fr;
    overflow-y: auto;
}

.card {
    background: #1e293b;
    border: round #334155;
    padding: 1 2;
    margin: 1 0;
}

.card-title {
    text-style: bold;
    color: #38bdf8;
    margin-bottom: 1;
}

.card-subtitle {
    color: #94a3b8;
    margin-bottom: 1;
}

.form-label {
    color: #cbd5e1;
    text-style: bold;
    margin-top: 1;
}

Input {
    background: #0f172a;
    border: tall #475569;
    color: #f8fafc;
    margin-bottom: 1;
}

Input:focus {
    border: tall #006a61;
}

Select {
    background: #0f172a;
    border: tall #475569;
    margin-bottom: 1;
}

Button {
    background: #006a61;
    color: #ffffff;
    text-style: bold;
    border: none;
    margin: 1 1 1 0;
}

Button:hover {
    background: #059669;
}

Button.-secondary {
    background: #334155;
    color: #f8fafc;
}

Button.-secondary:hover {
    background: #475569;
}

Button.-accent {
    background: #7c3aed;
    color: #ffffff;
}

Button.-accent:hover {
    background: #8b5cf6;
}

#split_left {
    width: 32%;
    border-right: solid #334155;
    height: 1fr;
    padding-right: 1;
}

#split_right {
    width: 68%;
    height: 1fr;
    padding-left: 1;
}

Tree {
    background: #0f172a;
    color: #f8fafc;
    border: round #334155;
    height: 1fr;
}

MarkdownViewer {
    background: #0f172a;
    height: 1fr;
    border: round #334155;
    padding: 0 1;
}

#status_message {
    padding: 1;
    margin-top: 1;
    border: round #334155;
    color: #38bdf8;
}

.badge {
    padding: 0 1;
    background: #006a61;
    color: #ffffff;
    text-style: bold;
}

.badge-tier1 {
    background: #7c3aed;
}

.badge-tier2 {
    background: #0284c7;
}

.badge-tier3 {
    background: #059669;
}

Checkbox {
    margin: 0 0 1 0;
}
"""
