import tkinter as tk


# Default Styles for Consistency
DEFAULT_STYLES = {
    "font": "Arial",
    "font_size": 12,
    "font_color": "white",
    "bg_color": "#6a0dad",
    "button_width": 20,
    "entry_width": 30,
    "pady": 10,
    "padx": 5,
}


def create_label(
    parent,
    text,
    font_size=DEFAULT_STYLES["font_size"],
    font_color=DEFAULT_STYLES["font_color"],
    bg_color=DEFAULT_STYLES["bg_color"],
    pady=DEFAULT_STYLES["pady"],
):
    """Create a styled label."""
    return tk.Label(
        parent,
        text=text,
        font=(DEFAULT_STYLES["font"], font_size),
        fg=font_color,
        bg=bg_color,
        pady=pady,
    )


def create_button(
    parent,
    text,
    command=None,
    font_size=DEFAULT_STYLES["font_size"],
    width=DEFAULT_STYLES["button_width"],
    pady=DEFAULT_STYLES["pady"],
    tooltip=None,
):
    """Create a styled button."""
    button = tk.Button(
        parent,
        text=text,
        font=(DEFAULT_STYLES["font"], font_size),
        width=width,
        command=command,
        pady=pady,
    )
    if tooltip:
        _add_tooltip(button, tooltip)
    return button


def create_entry(
    parent,
    show=None,
    font_size=DEFAULT_STYLES["font_size"],
    width=DEFAULT_STYLES["entry_width"],
    tooltip=None,
):
    """Create a styled entry field."""
    entry = tk.Entry(
        parent,
        font=(DEFAULT_STYLES["font"], font_size),
        width=width,
        show=show,
    )
    if tooltip:
        _add_tooltip(entry, tooltip)
    return entry


def create_frame(parent, bg_color=DEFAULT_STYLES["bg_color"], pady=DEFAULT_STYLES["pady"]):
    """Create a styled frame."""
    return tk.Frame(parent, bg=bg_color, pady=pady)


def clear_window(parent):
    """Clear all widgets from a given parent window."""
    try:
        for widget in parent.winfo_children():
            widget.destroy()
    except Exception as e:
        print(f"Error clearing window: {e}")


def _add_tooltip(widget, text):
    """Private function to add a tooltip to a widget."""
    tooltip = tk.Label(
        widget,
        text=text,
        font=(DEFAULT_STYLES["font"], 10),
        fg="black",
        bg="yellow",
        bd=1,
        relief="solid",
        wraplength=150,
    )
    tooltip.place_forget()

    def on_enter(event):
        tooltip.place(x=event.x_root + 10, y=event.y_root + 10)

    def on_leave(event):
        tooltip.place_forget()

    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)
