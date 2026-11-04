# Responsive and mobile patterns

Most traffic is a phone, held in one hand, on a network that drops. Design for
that and the desktop follows; design for the desktop and the phone is a compromise.

## Breakpoints that matter

| Width | Reality |
|---|---|
| 320-360 | The cheap Android floor. If it works here, it works. |
| 390-430 | Modern iPhone and Android flagships |
| 768 | Tablet portrait - usually a stretched phone, not a small desktop |
| 1024-1280 | Laptop |
| 1440+ | Desktop, and where a max-width container saves the layout |

Decide what *changes* at each, not "it is responsive".

## Layout rules

- **One column below 768.** Two columns on a phone halves both.
- **Max content width 60-75 characters.** A full-width paragraph on a 27-inch screen is unreadable.
- **Fluid type with a clamp**, not a fixed 16px everywhere: body scales 16-18, headings scale more.
- **Grid gap from the spacing scale**, so the rhythm holds across breakpoints.
- **Sticky elements eat the viewport.** One sticky header or one sticky CTA, never both on a phone.

## Mobile patterns that work

| Job | Pattern | Why |
|---|---|---|
| Primary action | Bottom-anchored, thumb reach | Top-right is unreachable one-handed |
| Long form | One question per screen, or a stepper | Abandonment drops with visible progress |
| Filters | Bottom sheet, applied with a count | A filter panel on a 360px screen is a maze |
| Navigation | 5 items maximum, labels always | Icons alone are guessed wrong |
| Destructive action | In a menu, with confirmation | Never beside the primary |
| Lists | 8-12 items, then load more with a real end state | Infinite scroll loses the footer and the back position |
| Search | Persistent field, recent searches | Typing on mobile is expensive |

## Keyboard, safe areas, gestures

- **Keyboard open**: the focused field scrolls into view, the CTA stays reachable, and the layout does not jump.
- **Safe areas**: respect the notch and the home indicator; text in the bottom 20% of a reel is eaten by the UI.
- **Gestures are shortcuts, never the only path.** Back-swipe must not be the only way out of a screen.
- **Pull to refresh** only where the data genuinely changes.

## Desktop specifics

- Hover states exist; do not rely on them for critical information.
- Tables earn their place above 1024; below that, a card per row.
- Keyboard shortcuts for power users, documented once, never required.
- Multi-column forms are faster on desktop - group by meaning, not by count.

## Performance is a design decision

- **Every image gets a budget** (a hero under 200KB), a width and height, and lazy loading below the fold.
- **Skeletons over spinners** - layout stability is a design property.
- **Fonts: two weights, subsetted, `font-display: swap`.** A slow font is a blank screen.
- **Third-party widgets** (chat, reviews, pixels) are the usual cause of a 6-second page. Ask what each one costs.

## Anti-patterns

- A desktop layout shrunk with `zoom`.
- Hover-only affordances on touch.
- A 100vh hero on a phone with a browser bar.
- Ten tap targets within 8dp of each other.
- Testing on a desktop with device emulation instead of a real phone.
