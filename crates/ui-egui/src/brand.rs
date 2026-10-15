//! Approved PWDS artwork for the FigStrike home and About surfaces.

use egui::{Color32, Rect, Sense, TextureHandle, TextureOptions, pos2, vec2};

static PWDS_MARK: &[u8] = include_bytes!("../../../assets/branding/PWDS-logo.png");
pub(crate) const MARK_ID: &str = "figstrike-pwds-mark";

fn mark(ctx: &egui::Context) -> Option<TextureHandle> {
    let id = egui::Id::new(MARK_ID);
    if let Some(texture) = ctx.data(|data| data.get_temp::<TextureHandle>(id)) {
        return Some(texture);
    }
    let bitmap = image::load_from_memory_with_format(PWDS_MARK, image::ImageFormat::Png).ok()?.to_rgba8();
    let pixels = egui::ColorImage::from_rgba_unmultiplied([bitmap.width() as usize, bitmap.height() as usize], bitmap.as_raw());
    let texture = ctx.load_texture(MARK_ID, pixels, TextureOptions::LINEAR);
    ctx.data_mut(|data| data.insert_temp(id, texture.clone()));
    Some(texture)
}

pub fn logo(ui: &egui::Ui, plaque: Rect) {
    ui.painter().rect_filled(plaque, 10.0, Color32::WHITE);
    if let Some(texture) = mark(ui.ctx()) {
        let width = plaque.width() - 20.0;
        let image = Rect::from_center_size(plaque.center(), vec2(width, width * 129.0 / 300.0));
        ui.painter().image(texture.id(), image, Rect::from_min_max(pos2(0.0, 0.0), pos2(1.0, 1.0)), Color32::WHITE);
    }
}

pub fn header(ui: &mut egui::Ui, subtitle: &str) {
    let width = ui.available_width().min(720.0);
    let (card, _) = ui.allocate_exact_size(vec2(width, 112.0), Sense::hover());
    ui.painter().rect_filled(card, 12.0, Color32::from_rgb(27, 36, 56));
    let plaque = Rect::from_min_size(card.min + vec2(16.0, 17.0), vec2(164.0, 78.0));
    logo(ui, plaque);
    ui.painter().text(card.min + vec2(198.0, 43.0), egui::Align2::LEFT_CENTER, "FigStrike", egui::FontId::proportional(25.0), Color32::WHITE);
    ui.painter().text(
        card.min + vec2(198.0, 76.0),
        egui::Align2::LEFT_CENTER,
        subtitle,
        egui::FontId::proportional(12.0),
        Color32::from_rgb(190, 202, 222),
    );
}
