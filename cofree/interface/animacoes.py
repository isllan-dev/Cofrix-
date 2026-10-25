def animate_page(app, frame):
    app.animating = True

    frame.place(
        relx=0,
        rely=0.04,
        relwidth=1,
        relheight=1,
    )

    def step(position=0):
        if not frame.winfo_exists():
            app.animating = False
            return

        progress = position / 8

        frame.place_configure(
            rely=0.04 * (1 - progress)
        )

        if position < 8:
            app.after(
                15,
                lambda: step(position + 1),
            )
        else:
            frame.place_forget()
            frame.grid(
                row=0,
                column=0,
                sticky="nsew",
            )
            app.animating = False

    step()