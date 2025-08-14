use leptos::prelude::*;

#[component]
pub fn NavigationBar(
    #[prop(into)] is_collapsed: ReadSignal<bool>,
    #[prop(into)] set_collapsed: WriteSignal<bool>,
) -> impl IntoView {
    view! {
        <nav class=move || format!("sidebar {}", if is_collapsed.get() { "collapsed" } else { "" })>
            <div class="sidebar-header">
                <button
                    class="toggle-btn"
                    on:click=move |_| set_collapsed.set(!is_collapsed.get())
                >
                    {move || if is_collapsed.get() { "→" } else { "←" }}
                </button>
            </div>

            <div class="nav-content">
                <ul class="nav-menu">
                    <li class="nav-item">
                        <span class="nav-label">"Metrics"</span>
                    </li>
                    <li class="nav-item">
                        <span class="nav-label">"Ads"</span>
                    </li>
                    <li class="nav-item">
                        <span class="nav-label">"Topics"</span>
                    </li>
                    <li class="nav-item">
                        <span class="nav-label">"Groups"</span>
                    </li>
                    <li class="nav-item">
                        <span class="nav-label">"Org Settings"</span>
                    </li>
                </ul>
            </div>
        </nav>
    }
}
